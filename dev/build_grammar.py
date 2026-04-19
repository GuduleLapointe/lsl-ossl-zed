#!/usr/bin/env python3
"""
Build grammar/grammar.js from the template and compile it with tree-sitter.

Usage:
    ./dev/build_grammar.py

Steps:
    1. Read grammar/src/grammar-template.js (human-editable template)
    2. Insert LSL/OSSL function, constant, and event lists from doc/*.md
    3. Write grammar/grammar.js (generated — do not edit by hand)
    4. Run `npm run build` in grammar/ to compile the parser
    5. Write grammar/.stats for use by deploy-grammar.sh

Prerequisites: run generate_ref_docs.py first to populate doc/.
"""

import json
import re
import subprocess
import sys
from pathlib import Path


def extract_names(md_path, sig_pattern=None):
    """Return sorted function/constant/event names from a Markdown reference file.

    Collects ### Name headers, plus any names matched by sig_pattern on
    signature bullet lines only (lines starting with '- `'), to avoid
    false positives from function names mentioned in description text.
    """
    text = md_path.read_text(encoding="utf-8")
    names = set(re.findall(r"^### (\w+)", text, re.MULTILINE))
    if sig_pattern:
        for line in text.splitlines():
            if line.startswith("- `"):
                for m in re.finditer(sig_pattern, line):
                    names.add(m.group(1))
    return sorted(names, key=str.lower)


def make_choice(names, depth=3):
    """Render a tree-sitter choice(...) block at the given tab depth."""
    t = "\t" * depth
    ti = "\t" * (depth + 1)
    items = "\n".join(f'{ti}"{name}",' for name in sorted(names, key=str.lower))
    return f"choice(\n{items}\n{t}),"


def replace_placeholder(js, rule_name, names):
    """Replace a placeholder choice() in the template with the full choice(...) block.

    Matches lines of the form (2-tab indent):
        \t\trule_name: ($) => choice(), // WHATEVER_PLACEHOLDER
    and replaces them with the expanded multi-line choice(...) block.
    """
    pattern = re.compile(
        rf"^(\t\t{re.escape(rule_name)}: \(\$\) =>)\s*choice\(\),.*$",
        re.MULTILINE,
    )
    new_choice = make_choice(names, depth=3)

    def repl(m):
        return f"{m.group(1)}\n\t\t\t{new_choice}"

    result, count = pattern.subn(repl, js)
    if count == 0:
        print(f"⚠️  Placeholder for '{rule_name}' not found in template")
    return result


def parse_doc_sections(md_path):
    """Parse a doc .md file into a list of {name, signatures, desc} dicts."""
    text = md_path.read_text(encoding="utf-8")
    entries = []
    parts = re.split(r"^### (\w+)\n", text, flags=re.MULTILINE)
    for i in range(1, len(parts), 2):
        name = parts[i]
        body = parts[i + 1] if i + 1 < len(parts) else ""
        sigs = re.findall(r"^- `([^`]+)`", body, re.MULTILINE)
        desc = ""
        past_sigs = False
        for line in body.splitlines():
            s = line.strip()
            if s.startswith("- `"):
                past_sigs = True
            elif past_sigs and s and not s.startswith("-") \
                    and not s.startswith("Source:") and not s.startswith("Generated:"):
                desc = s
                break
        entries.append({"name": name, "signatures": sigs, "desc": desc})
    return entries


def update_event_snippets(doc_dir, snippets_path):
    """Add any missing event handler snippets to snippets/lsl-ossl.json.

    Existing entries (with hand-written descriptions) are never modified.
    New events found in the doc get a generic auto-generated entry.
    """
    events = parse_doc_sections(doc_dir / "LSL_Events.md")
    snippets = json.loads(snippets_path.read_text(encoding="utf-8"))

    added = []
    for event in events:
        name = event["name"]
        if name in snippets:
            continue
        sig = event["signatures"][0] if event["signatures"] else f"{name}()"
        snippets[name] = {
            "prefix": name,
            "body": [sig, "{", "\t$0", "}"],
            "description": f"LSL {name} event handler",
        }
        added.append(name)

    if added:
        snippets_path.write_text(
            json.dumps(snippets, indent="\t") + "\n", encoding="utf-8"
        )
        print(f"✅ {len(added):4d}  event snippets added   → {snippets_path}: {', '.join(added)}")
    else:
        print(f"✅       Event snippets up to date → {snippets_path}")


def generate_completions(doc_dir, output_path):
    """Generate lsp/completions.json from doc/*.md for LSP completion support."""
    lsl_entries  = parse_doc_sections(doc_dir / "LSL_Functions.md")
    ossl_entries = parse_doc_sections(doc_dir / "OSSL_Functions.md")
    const_entries = parse_doc_sections(doc_dir / "LSL_Constants.md")

    functions = (
        [{"name": e["name"], "kind": "lsl",  "signatures": e["signatures"], "desc": e["desc"]} for e in lsl_entries] +
        [{"name": e["name"], "kind": "ossl", "signatures": e["signatures"], "desc": e["desc"]} for e in ossl_entries]
    )

    constants = []
    for e in const_entries:
        if not e["signatures"]:
            continue
        sig = e["signatures"][0]  # e.g. "integer TRUE = 1"
        m = re.match(r"(\w+)\s+\w+(?:\s*=\s*(.+))?", sig)
        constants.append({
            "name":  e["name"],
            "type":  m.group(1) if m else "",
            "value": (m.group(2) or "").strip() if m else "",
        })

    data = {"functions": functions, "constants": constants}
    output_path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    print(f"✅ {len(functions):4d}  functions  → {output_path}")
    print(f"✅ {len(constants):4d}  constants  → {output_path}")


def main():
    doc_dir = Path("doc")
    template_path = Path("grammar/src/grammar-template.js")
    grammar_path = Path("grammar/grammar.js")
    completions_path = Path("lsp/completions.json")
    stats_path = Path("logs/build_grammar.stats.json")
    stats_path.parent.mkdir(exist_ok=True)

    missing = [p for p in [
        doc_dir / "LSL_Functions.md",
        doc_dir / "OSSL_Functions.md",
        doc_dir / "LSL_Constants.md",
        doc_dir / "LSL_Events.md",
        template_path,
    ] if not p.exists()]
    if missing:
        for p in missing:
            print(f"❌ Not found: {p}")
        sys.exit(1)

    lsl_names  = set(extract_names(doc_dir / "LSL_Functions.md",
                                   sig_pattern=r"\b(ll[A-Za-z]\w+)\s*\("))
    ossl_names = set(extract_names(doc_dir / "OSSL_Functions.md",
                                   sig_pattern=r"\b(os[A-Za-z]\w+)\s*\("))

    lsl_funcs  = sorted(lsl_names,  key=str.lower)
    ossl_funcs = sorted(ossl_names, key=str.lower)
    constants  = extract_names(doc_dir / "LSL_Constants.md")
    events     = extract_names(doc_dir / "LSL_Events.md")

    # Generate grammar.js from template
    js = template_path.read_text(encoding="utf-8")
    js = replace_placeholder(js, "constant",      constants)
    js = replace_placeholder(js, "lsl_function",  lsl_funcs)
    js = replace_placeholder(js, "ossl_function", ossl_funcs)
    js = replace_placeholder(js, "event_name",    events)
    grammar_path.write_text(js, encoding="utf-8")

    print(f"✅ {len(lsl_funcs):4d}  LSL functions   → grammar/grammar.js")
    print(f"✅ {len(ossl_funcs):4d}  OSSL functions  → grammar/grammar.js")
    print(f"✅ {len(constants):4d}  constants       → grammar/grammar.js")
    print(f"✅ {len(events):4d}  events          → grammar/grammar.js")

    # Add any missing event snippets
    update_event_snippets(doc_dir, Path("snippets/lsl-ossl.json"))

    # Generate completions data for LSP
    generate_completions(doc_dir, completions_path)

    # Compile parser
    print("==> Running npm run build in grammar/…")
    subprocess.run(["npm", "run", "build"], cwd="grammar", check=True)
    print("✅ Parser compiled")

    # Write stats for deploy step
    stats = {
        "lsl_functions": len(lsl_funcs),
        "ossl_functions": len(ossl_funcs),
        "constants": len(constants),
        "events": len(events),
    }
    stats_path.write_text(json.dumps(stats, indent=2) + "\n", encoding="utf-8")
    print(f"✅ Stats written → {stats_path}")


if __name__ == "__main__":
    main()
