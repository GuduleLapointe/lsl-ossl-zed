fn main() {
    cc::Build::new()
        .file("../grammar/src/parser.c")
        .include("../grammar/src")
        .compile("tree-sitter-lsl");
}
