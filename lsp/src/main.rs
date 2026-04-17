use std::io::{self, BufRead, Write};
use serde::{Deserialize, Serialize};
use serde_json::{json, Value};

// ─── tree-sitter language binding ────────────────────────────────────────────

extern "C" {
    fn tree_sitter_lsl() -> tree_sitter::Language;
}

fn lsl_language() -> tree_sitter::Language {
    unsafe { tree_sitter_lsl() }
}

// ─── LSP JSON-RPC transport ───────────────────────────────────────────────────

#[derive(Debug, Deserialize, Serialize)]
struct RpcMessage {
    jsonrpc: String,
    #[serde(skip_serializing_if = "Option::is_none")]
    id: Option<Value>,
    #[serde(skip_serializing_if = "Option::is_none")]
    method: Option<String>,
    #[serde(skip_serializing_if = "Option::is_none")]
    params: Option<Value>,
    #[serde(skip_serializing_if = "Option::is_none")]
    result: Option<Value>,
    #[serde(skip_serializing_if = "Option::is_none")]
    error: Option<Value>,
}

fn read_message(reader: &mut impl BufRead) -> Option<RpcMessage> {
    let mut content_length: usize = 0;
    loop {
        let mut line = String::new();
        reader.read_line(&mut line).ok()?;
        let line = line.trim_end_matches(['\r', '\n']);
        if line.is_empty() {
            break;
        }
        if let Some(val) = line.strip_prefix("Content-Length: ") {
            content_length = val.trim().parse().ok()?;
        }
    }
    if content_length == 0 {
        return None;
    }
    let mut buf = vec![0u8; content_length];
    reader.read_exact(&mut buf).ok()?;
    serde_json::from_slice(&buf).ok()
}

fn send_response(writer: &mut impl Write, id: Value, result: Value) {
    let msg = RpcMessage {
        jsonrpc: "2.0".into(),
        id: Some(id),
        method: None,
        params: None,
        result: Some(result),
        error: None,
    };
    let body = serde_json::to_string(&msg).unwrap();
    write!(writer, "Content-Length: {}\r\n\r\n{}", body.len(), body).unwrap();
    writer.flush().unwrap();
}

fn send_error(writer: &mut impl Write, id: Value, code: i64, message: &str) {
    let msg = RpcMessage {
        jsonrpc: "2.0".into(),
        id: Some(id),
        method: None,
        params: None,
        result: None,
        error: Some(json!({ "code": code, "message": message })),
    };
    let body = serde_json::to_string(&msg).unwrap();
    write!(writer, "Content-Length: {}\r\n\r\n{}", body.len(), body).unwrap();
    writer.flush().unwrap();
}

// ─── LSL Formatter ───────────────────────────────────────────────────────────

struct Formatter<'a> {
    source: &'a [u8],
    out: String,
    indent: usize,
    /// Whether we're at the start of a fresh line (only indent written so far).
    at_line_start: bool,
}

impl<'a> Formatter<'a> {
    fn new(source: &'a [u8]) -> Self {
        Self {
            source,
            out: String::new(),
            indent: 0,
            at_line_start: true,
        }
    }

    fn text(&self, node: tree_sitter::Node) -> String {
        node.utf8_text(self.source).unwrap_or("").to_owned()
    }

    fn push_indent(&mut self) {
        for _ in 0..self.indent {
            self.out.push('\t');
        }
    }

    fn newline(&mut self) {
        self.out.push('\n');
        self.at_line_start = true;
    }

    fn ensure_newline(&mut self) {
        if !self.at_line_start {
            self.newline();
        }
    }

    fn write(&mut self, s: &str) {
        if self.at_line_start && !s.is_empty() {
            self.push_indent();
            self.at_line_start = false;
        }
        self.out.push_str(s);
    }

    /// Emit a blank separator line (only if we're not already at the start of the file).
    fn blank_line(&mut self) {
        if !self.out.is_empty() && !self.out.ends_with("\n\n") {
            self.ensure_newline();
            self.newline();
        }
    }

    // ── Node formatters ──────────────────────────────────────────────────────

    fn format_node(&mut self, node: tree_sitter::Node) {
        if node.is_error() || node.kind() == "ERROR" {
            let t = self.text(node);
            self.write(&t);
            return;
        }

        match node.kind() {
            "source_file" => self.fmt_source_file(node),
            "comment" => self.fmt_comment(node),
            "variable_declaration" => self.fmt_variable_declaration(node),
            "function_definition" => self.fmt_function_definition(node),
            "state_definition" => self.fmt_state_definition(node),
            "event_handler" => self.fmt_event_handler(node),
            "block" => self.fmt_block(node),
            "if_statement" => self.fmt_if_statement(node),
            "for_statement" => self.fmt_for_statement(node),
            "while_statement" => self.fmt_while_statement(node),
            "return_statement" => self.fmt_return_statement(node),
            "jump_statement" => self.fmt_jump_statement(node),
            "expression_statement" => self.fmt_expression_statement(node),
            "expression" => self.fmt_expression(node),
            "assignment" => self.fmt_assignment(node),
            "binary_expression" => self.fmt_binary_expression(node),
            "cast_expression" => self.fmt_cast_expression(node),
            "call_expression" => self.fmt_call_expression(node),
            "argument_list" => self.fmt_argument_list(node),
            "vector_literal" => self.fmt_vector_literal(node),
            "rotation_literal" => self.fmt_rotation_literal(node),
            "list_literal" => self.fmt_list_literal(node),
            "parameter_list" => self.fmt_parameter_list(node),
            "parameter" => self.fmt_parameter(node),
            // Leaf tokens
            _ => {
                let t = self.text(node);
                self.write(&t);
            }
        }
    }

    fn fmt_source_file(&mut self, node: tree_sitter::Node) {
        let mut cursor = node.walk();
        let children: Vec<_> = node.children(&mut cursor).collect();
        let mut first = true;
        for child in children {
            if child.kind() == "comment" {
                self.ensure_newline();
                self.format_node(child);
                self.newline();
                first = false;
            } else {
                // Blank line between top-level declarations
                if !first {
                    self.blank_line();
                }
                self.ensure_newline();
                self.format_node(child);
                self.newline();
                first = false;
            }
        }
    }

    fn fmt_comment(&mut self, node: tree_sitter::Node) {
        let t = self.text(node);
        self.write(&t);
    }

    fn fmt_variable_declaration(&mut self, node: tree_sitter::Node) {
        // type identifier [= expression] ;
        let mut cursor = node.walk();
        let children: Vec<_> = node.children(&mut cursor).collect();
        for (i, child) in children.iter().enumerate() {
            match child.kind() {
                ";" => self.out.push(';'),
                "=" => self.out.push_str(" = "),
                "type" => {
                    self.format_node(*child);
                    self.out.push(' ');
                }
                "identifier" => {
                    self.format_node(*child);
                }
                "expression" => {
                    self.format_node(*child);
                }
                "comment" => {
                    if i > 0 { self.out.push(' '); }
                    self.format_node(*child);
                }
                _ => self.format_node(*child),
            }
        }
    }

    fn fmt_function_definition(&mut self, node: tree_sitter::Node) {
        // type identifier ( [parameter_list] ) block
        let mut cursor = node.walk();
        let children: Vec<_> = node.children(&mut cursor).collect();
        for child in &children {
            match child.kind() {
                "type" => {
                    self.format_node(*child);
                    self.out.push(' ');
                }
                "identifier" => self.format_node(*child),
                "(" => self.out.push('('),
                ")" => self.out.push(')'),
                "parameter_list" => self.format_node(*child),
                "block" => {
                    self.newline();
                    self.ensure_newline();
                    self.format_node(*child);
                }
                _ => self.format_node(*child),
            }
        }
    }

    fn fmt_state_definition(&mut self, node: tree_sitter::Node) {
        // "default" block  |  "state" identifier block
        let mut cursor = node.walk();
        let children: Vec<_> = node.children(&mut cursor).collect();
        for child in &children {
            match child.kind() {
                "default" => self.write("default"),
                "state" => self.write("state"),
                "identifier" => {
                    self.out.push(' ');
                    self.format_node(*child);
                }
                "block" => {
                    self.newline();
                    self.ensure_newline();
                    self.format_node(*child);
                }
                _ => self.format_node(*child),
            }
        }
    }

    fn fmt_event_handler(&mut self, node: tree_sitter::Node) {
        // event_name ( [parameter_list] ) [comment] block
        let mut cursor = node.walk();
        let children: Vec<_> = node.children(&mut cursor).collect();
        for child in &children {
            match child.kind() {
                "event_name" => self.format_node(*child),
                "(" => self.out.push('('),
                ")" => self.out.push(')'),
                "parameter_list" => self.format_node(*child),
                "block" => {
                    self.newline();
                    self.ensure_newline();
                    self.format_node(*child);
                }
                "comment" => {
                    self.out.push(' ');
                    self.format_node(*child);
                }
                _ => self.format_node(*child),
            }
        }
    }

    fn fmt_block(&mut self, node: tree_sitter::Node) {
        // { statements }
        self.write("{");
        self.newline();
        self.indent += 1;

        let mut cursor = node.walk();
        let children: Vec<_> = node.children(&mut cursor).collect();
        // Skip the `{` and `}` tokens (first and last children)
        let inner = &children[1..children.len().saturating_sub(1)];

        let mut prev_was_handler = false;
        for child in inner {
            if child.kind() == "comment" {
                self.ensure_newline();
                self.format_node(*child);
                self.newline();
            } else {
                let is_handler = matches!(child.kind(), "event_handler" | "function_definition");
                if is_handler && prev_was_handler {
                    self.blank_line();
                }
                self.ensure_newline();
                self.format_node(*child);
                self.newline();
                prev_was_handler = is_handler;
            }
        }

        self.indent -= 1;
        self.ensure_newline();
        self.write("}");
    }

    fn fmt_if_statement(&mut self, node: tree_sitter::Node) {
        // if ( expression ) _body [else _body]
        // Parse children positionally: after ")" we collect optional trailing
        // comments (kept inline), then one body, then optionally "else" + body.
        let mut cursor = node.walk();
        let children: Vec<_> = node.children(&mut cursor).collect();

        // Phase 1: emit "if ( expr )"
        self.write("if (");
        let close_paren = children.iter().position(|c| c.kind() == ")").unwrap_or(3);
        let expr_node = children.iter().find(|c| c.kind() == "expression");
        if let Some(e) = expr_node {
            self.format_node(*e);
        }
        self.out.push(')');

        // Phase 2: optional inline comment(s) after ")", then body
        let after_paren = &children[close_paren + 1..];
        let else_pos = after_paren.iter().position(|c| c.kind() == "else");
        let then_slice = match else_pos {
            Some(p) => &after_paren[..p],
            None => after_paren,
        };

        // Inline comments before the body
        for c in then_slice {
            if c.kind() == "comment" {
                self.out.push(' ');
                self.fmt_comment(*c);
            }
        }
        // The body itself (last non-comment in then_slice)
        if let Some(body) = then_slice.iter().rev().find(|c| c.kind() != "comment") {
            self.fmt_body(*body, false);
        }

        // Phase 3: optional else
        if let Some(ep) = else_pos {
            let else_slice = &after_paren[ep + 1..];
            self.ensure_newline();
            self.write("else");

            // Inline comments between "else" and its body
            for c in else_slice {
                if c.kind() == "comment" {
                    self.out.push(' ');
                    self.fmt_comment(*c);
                }
            }
            if let Some(body) = else_slice.iter().rev().find(|c| c.kind() != "comment") {
                if body.kind() == "if_statement" {
                    self.out.push(' ');
                    self.format_node(*body);
                } else {
                    self.fmt_body(*body, true);
                }
            }
        }
    }

    /// Format a body (_body = block | single statement).
    /// `after_else` means we already wrote " else" so a block stays on same line.
    fn fmt_body(&mut self, node: tree_sitter::Node, after_else: bool) {
        if node.kind() == "block" {
            if after_else {
                self.out.push(' ');
                // Inline opening brace for else blocks
                self.fmt_block_inline(node);
            } else {
                self.newline();
                self.ensure_newline();
                self.format_node(node);
            }
        } else {
            // Single statement without braces
            self.newline();
            self.indent += 1;
            self.ensure_newline();
            self.format_node(node);
            self.newline();
            self.indent -= 1;
        }
    }

    /// Like fmt_block but opening brace is on the current line (for else {).
    fn fmt_block_inline(&mut self, node: tree_sitter::Node) {
        self.out.push('{');
        self.newline();
        self.indent += 1;

        let mut cursor = node.walk();
        let children: Vec<_> = node.children(&mut cursor).collect();
        let inner = &children[1..children.len().saturating_sub(1)];

        for child in inner {
            self.ensure_newline();
            self.format_node(*child);
            self.newline();
        }

        self.indent -= 1;
        self.ensure_newline();
        self.write("}");
    }

    fn fmt_for_statement(&mut self, node: tree_sitter::Node) {
        // for ( [expr] ; [expr] ; [expr] ) _body
        let mut cursor = node.walk();
        let children: Vec<_> = node.children(&mut cursor).collect();
        let mut i = 0;
        while i < children.len() {
            let child = children[i];
            match child.kind() {
                "for" => {
                    self.write("for");
                    self.out.push(' ');
                }
                "(" => self.out.push('('),
                ")" => {
                    self.out.push(')');
                    // next is the body
                    if let Some(body) = children.get(i + 1) {
                        self.fmt_body(*body, false);
                        i += 2;
                        continue;
                    }
                }
                ";" => self.out.push_str("; "),
                "expression" => self.format_node(child),
                _ => {}
            }
            i += 1;
        }
    }

    fn fmt_while_statement(&mut self, node: tree_sitter::Node) {
        // while ( expression ) _body
        let mut cursor = node.walk();
        let children: Vec<_> = node.children(&mut cursor).collect();
        let mut i = 0;
        while i < children.len() {
            let child = children[i];
            match child.kind() {
                "while" => {
                    self.write("while");
                    self.out.push(' ');
                }
                "(" => self.out.push('('),
                ")" => {
                    self.out.push(')');
                    if let Some(body) = children.get(i + 1) {
                        self.fmt_body(*body, false);
                        i += 2;
                        continue;
                    }
                }
                "expression" => self.format_node(child),
                _ => {}
            }
            i += 1;
        }
    }

    fn fmt_return_statement(&mut self, node: tree_sitter::Node) {
        self.write("return");
        if let Some(expr) = node.named_child(0) {
            self.out.push(' ');
            self.format_node(expr);
        }
        self.out.push(';');
    }

    fn fmt_jump_statement(&mut self, node: tree_sitter::Node) {
        // "jump" identifier ";" or "state" identifier ";"
        let mut cursor = node.walk();
        let children: Vec<_> = node.children(&mut cursor).collect();
        for (i, child) in children.iter().enumerate() {
            match child.kind() {
                "jump" => self.write("jump"),
                "state" => self.write("state"),
                "identifier" => {
                    if i > 0 { self.out.push(' '); }
                    self.format_node(*child);
                }
                ";" => self.out.push(';'),
                _ => {}
            }
        }
    }

    fn fmt_expression_statement(&mut self, node: tree_sitter::Node) {
        if let Some(expr) = node.named_child(0) {
            self.format_node(expr);
        }
        self.out.push(';');
    }

    fn fmt_expression(&mut self, node: tree_sitter::Node) {
        // expression is a transparent wrapper — format the single child
        if let Some(child) = node.named_child(0) {
            self.format_node(child);
        } else {
            // Leaf expression (identifier, number, string, constant, lsl_function, ossl_function)
            let t = self.text(node);
            if !self.at_line_start {
                self.out.push_str(&t);
            } else {
                self.write(&t);
            }
        }
    }

    fn fmt_assignment(&mut self, node: tree_sitter::Node) {
        // identifier = expression
        let mut cursor = node.walk();
        let children: Vec<_> = node.children(&mut cursor).collect();
        for child in &children {
            match child.kind() {
                "=" => self.out.push_str(" = "),
                "identifier" => self.format_node(*child),
                "expression" => self.format_node(*child),
                _ => self.format_node(*child),
            }
        }
    }

    fn fmt_binary_expression(&mut self, node: tree_sitter::Node) {
        // expression op expression
        let mut cursor = node.walk();
        let children: Vec<_> = node.children(&mut cursor).collect();
        for (i, child) in children.iter().enumerate() {
            if i == 0 {
                self.format_node(*child);
            } else if i == 1 {
                // operator
                let op = self.text(*child);
                self.out.push(' ');
                self.out.push_str(&op);
                self.out.push(' ');
            } else {
                self.format_node(*child);
            }
        }
    }

    fn fmt_cast_expression(&mut self, node: tree_sitter::Node) {
        // ( type ) expression
        self.out.push('(');
        if let Some(t) = node.child_by_field_name("type").or_else(|| node.named_child(0)) {
            self.format_node(t);
        }
        self.out.push(')');
        if let Some(expr) = node.named_child(1) {
            self.format_node(expr);
        }
    }

    fn fmt_call_expression(&mut self, node: tree_sitter::Node) {
        // function ( [argument_list] )
        if let Some(func) = node.child_by_field_name("function") {
            let t = self.text(func);
            if self.at_line_start {
                self.write(&t);
            } else {
                self.out.push_str(&t);
            }
        }
        self.out.push('(');
        if let Some(args) = node.named_child(1) {
            if args.kind() == "argument_list" {
                self.format_node(args);
            }
        }
        self.out.push(')');
    }

    fn fmt_argument_list(&mut self, node: tree_sitter::Node) {
        // expression (, expression)*
        let mut cursor = node.walk();
        let children: Vec<_> = node.children(&mut cursor).collect();
        let mut first = true;
        for child in &children {
            if child.kind() == "," {
                self.out.push_str(", ");
                first = false;
            } else {
                let _ = first;
                self.format_node(*child);
                first = false;
            }
        }
    }

    fn fmt_vector_literal(&mut self, node: tree_sitter::Node) {
        // < expr , expr , expr >
        let mut cursor = node.walk();
        let children: Vec<_> = node.children(&mut cursor).collect();
        for (i, child) in children.iter().enumerate() {
            match child.kind() {
                "<" => self.out.push('<'),
                ">" => self.out.push('>'),
                "," => self.out.push_str(", "),
                _ => {
                    let _ = i;
                    self.format_node(*child);
                }
            }
        }
    }

    fn fmt_rotation_literal(&mut self, node: tree_sitter::Node) {
        // < expr , expr , expr , expr >
        let mut cursor = node.walk();
        let children: Vec<_> = node.children(&mut cursor).collect();
        for child in &children {
            match child.kind() {
                "<" => self.out.push('<'),
                ">" => self.out.push('>'),
                "," => self.out.push_str(", "),
                _ => self.format_node(*child),
            }
        }
    }

    fn fmt_list_literal(&mut self, node: tree_sitter::Node) {
        // [ expr (, expr)* ]
        let mut cursor = node.walk();
        let children: Vec<_> = node.children(&mut cursor).collect();
        for child in &children {
            match child.kind() {
                "[" => self.out.push('['),
                "]" => self.out.push(']'),
                "," => self.out.push_str(", "),
                _ => self.format_node(*child),
            }
        }
    }

    fn fmt_parameter_list(&mut self, node: tree_sitter::Node) {
        let mut cursor = node.walk();
        let children: Vec<_> = node.children(&mut cursor).collect();
        for child in &children {
            if child.kind() == "," {
                self.out.push_str(", ");
            } else {
                self.format_node(*child);
            }
        }
    }

    fn fmt_parameter(&mut self, node: tree_sitter::Node) {
        // type identifier
        let mut cursor = node.walk();
        let children: Vec<_> = node.children(&mut cursor).collect();
        for (i, child) in children.iter().enumerate() {
            if i > 0 { self.out.push(' '); }
            self.format_node(*child);
        }
    }
}

// ─── Public format entry point ────────────────────────────────────────────────

pub fn format_lsl_with_parser(parser: &mut tree_sitter::Parser, source: &str) -> String {
    let tree = parser.parse(source, None).expect("Parse failed");
    let root = tree.root_node();

    let mut fmt = Formatter::new(source.as_bytes());
    fmt.format_node(root);

    // Ensure single trailing newline
    let mut result = fmt.out;
    while result.ends_with("\n\n") {
        result.pop();
    }
    if !result.ends_with('\n') {
        result.push('\n');
    }
    result
}

// ─── LSP server ──────────────────────────────────────────────────────────────

use std::collections::HashMap;

struct Server {
    /// Full text of each open document, keyed by URI.
    documents: HashMap<String, String>,
    parser: tree_sitter::Parser,
}

impl Server {
    fn new() -> Self {
        let mut parser = tree_sitter::Parser::new();
        parser.set_language(&lsl_language()).expect("Failed to load LSL language");
        Self {
            documents: HashMap::new(),
            parser,
        }
    }

    fn run(&mut self) {
        let stdin = io::stdin();
        let stdout = io::stdout();
        let mut reader = io::BufReader::new(stdin.lock());
        let mut writer = io::BufWriter::new(stdout.lock());

        while let Some(msg) = read_message(&mut reader) {
            let method = msg.method.as_deref().unwrap_or("");
            match method {
                "initialize" => {
                    let id = msg.id.unwrap_or(Value::Null);
                    send_response(
                        &mut writer,
                        id,
                        json!({
                            "capabilities": {
                                "textDocumentSync": {
                                    "openClose": true,
                                    "change": 1  // Full sync
                                },
                                "documentFormattingProvider": true
                            },
                            "serverInfo": { "name": "lsl-lsp", "version": "0.1.0" }
                        }),
                    );
                }
                "initialized" => {}
                "textDocument/didOpen" => {
                    let params = msg.params.unwrap_or(Value::Null);
                    if let (Some(uri), Some(text)) = (
                        params["textDocument"]["uri"].as_str(),
                        params["textDocument"]["text"].as_str(),
                    ) {
                        self.documents.insert(uri.to_string(), text.to_string());
                    }
                }
                "textDocument/didChange" => {
                    let params = msg.params.unwrap_or(Value::Null);
                    if let Some(uri) = params["textDocument"]["uri"].as_str() {
                        // We use full sync (kind=1), so the first change has the complete text.
                        if let Some(text) = params["contentChanges"][0]["text"].as_str() {
                            self.documents.insert(uri.to_string(), text.to_string());
                        }
                    }
                }
                "textDocument/didClose" => {
                    let params = msg.params.unwrap_or(Value::Null);
                    if let Some(uri) = params["textDocument"]["uri"].as_str() {
                        self.documents.remove(uri);
                    }
                }
                "textDocument/formatting" => {
                    let id = msg.id.unwrap_or(Value::Null);
                    let params = msg.params.unwrap_or(Value::Null);
                    let uri = params["textDocument"]["uri"].as_str().unwrap_or("");

                    if let Some(text) = self.documents.get(uri).cloned() {
                        let formatted = format_lsl_with_parser(&mut self.parser, &text);
                        if formatted == text {
                            send_response(&mut writer, id, json!([]));
                            continue;
                        }
                        let line_count = text.lines().count() as u64;
                        let last_col =
                            text.lines().last().map(|l| l.len()).unwrap_or(0) as u64;
                        send_response(
                            &mut writer,
                            id,
                            json!([{
                                "range": {
                                    "start": { "line": 0, "character": 0 },
                                    "end":   { "line": line_count, "character": last_col }
                                },
                                "newText": formatted
                            }]),
                        );
                    } else {
                        send_response(&mut writer, id, json!([]));
                    }
                }
                "shutdown" => {
                    let id = msg.id.unwrap_or(Value::Null);
                    send_response(&mut writer, id, Value::Null);
                }
                "exit" => break,
                _ => {
                    if let Some(id) = msg.id {
                        send_error(&mut writer, id, -32601, "Method not found");
                    }
                }
            }
        }
    }
}

fn main() {
    Server::new().run();
}

// ─── Tests ───────────────────────────────────────────────────────────────────

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_format_lsl() {
        let src = std::fs::read_to_string("../tests/test.lsl").unwrap();
        let mut parser = tree_sitter::Parser::new();
        parser.set_language(&lsl_language()).unwrap();
        let result = format_lsl_with_parser(&mut parser, &src);
        // Should be idempotent on second pass
        let result2 = format_lsl_with_parser(&mut parser, &result);
        assert_eq!(result, result2, "Formatter is not idempotent");
    }
}
