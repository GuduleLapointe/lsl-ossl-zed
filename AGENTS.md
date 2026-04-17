# Agents instructions

## Project Overview

This is a **Zed IDE extension** providing language support for **LSL (Linden Scripting Language)** and **OSSL (OpenSimulator Scripting Language)**. The extension uses tree-sitter for parsing and provides syntax highlighting, structural analysis, and language intelligence for Second Life/OpenSimulator scripting.

## Project Structure

```
lsl-ossl-zed/
├── Cargo.toml                    # Rust project configuration (Zed extension API)
├── extension.toml                # Zed extension metadata + grammar reference
├── src/
│   └── lib.rs                    # Rust extension entry point (zed_extension_api)
├── grammar/                      # Git submodule → tree-sitter-lsl-ossl
│   ├── grammar.js                # Tree-sitter grammar definition
│   └── src/parser.c              # Generated C parser (committed)
├── languages/lsl-ossl/
│   ├── config.toml               # Language config (grammar = "lsl")
│   └── highlights.scm            # Syntax highlighting queries
├── tests/
│   ├── test.lsl
│   └── test.ossl
├── snippets/                     # (future)
└── themes/                       # (future)
```

## Two-repo Architecture

The grammar and the Zed extension are in separate repos:

- **[tree-sitter-lsl-ossl](https://github.com/GuduleLapointe/tree-sitter-lsl-ossl)** — pure tree-sitter grammar (grammar.js + generated src/parser.c)
- **[lsl-ossl-zed](https://github.com/GuduleLapointe/lsl-ossl-zed)** — this repo: Zed extension (Rust + language config + highlighting)

`grammar/` is a git submodule pointing to tree-sitter-lsl-ossl. `extension.toml` references the grammar by GitHub URL + commit hash — **the hash must be updated every time the grammar repo is updated** (see DEVELOPERS.md for the full workflow).

## Essential Commands

### Building
- **Check Rust**: `cargo check`
- **Build extension**: `cargo build --target wasm32-wasip2`
- **Regenerate parser** (after grammar changes): `cd grammar && tree-sitter generate`

### Grammar deploy
- Full deploy (generate + commit + push + update hash): `./deploy-grammar.sh ["message"]`
- Default message: last grammar commit summary, e.g. `"deploy grammar abc1234 Fix something"`

### Zed development
- Install dev extension: Zed → Extensions → Install Dev Extension → point to this folder
- After changes: use "Rebuild Extension" in Zed's extension panel
- Open test files: `zed tests/test.lsl tests/test.ossl`
- No CLI command for Rebuild — must be done from Zed UI

## Language Support Files

| File | Purpose |
|------|---------|
| `grammar/grammar.js` | Tree-sitter grammar (edit this to change parsing) |
| `grammar/src/parser.c` | Generated — do not edit manually, run `tree-sitter generate` |
| `languages/lsl-ossl/highlights.scm` | Syntax highlighting queries |
| `languages/lsl-ossl/config.toml` | File extensions, tab size, comment style |
| `extension.toml` | Grammar repo URL + commit hash |
| `src/lib.rs` | Zed extension registration; future LSP client code goes here |

## Language Architecture

### Supported Languages
- **LSL (.lsl)**: Linden Scripting Language for Second Life
- **OSSL (.ossl)**: OpenSimulator Scripting Language extensions

### Key Language Features
- States: `default` and custom state definitions
- Events: `state_entry`, `touch_start`, `timer`, etc.
- Control flow: `if`, `for`, `while`, `return`, `jump`
- Functions: user-defined and built-in (`ll*` prefix for LSL, `os*` for OSSL)
- Types: `integer`, `float`, `string`, `key`, `vector`, `rotation`, `list`
- Constants: `TRUE`, `FALSE`, `PI`, `NULL_KEY`, `ZERO_VECTOR`, `ZERO_ROTATION`, etc.
- Comments: `//` single-line and `/* */` block comments

## Development Workflow

### Grammar changes
1. Edit `grammar/grammar.js`
2. `cd grammar && tree-sitter generate`
3. Commit + push in grammar submodule
4. Update `commit` hash in `extension.toml`
5. Commit extension repo

### Highlighting changes
Edit `languages/lsl-ossl/highlights.scm` — no parser regeneration needed.

### Rust/LSP changes
Edit `src/lib.rs` — Zed will recompile on next "Rebuild Extension".

## Important Notes

- `grammar = "lsl"` in config.toml must match `name:` in grammar.js (`name: "lsl"`)
- `[grammars.lsl]` key in extension.toml must also match
- The commit hash in extension.toml must be updated after every grammar push
- `wasm32-wasip2` target must be installed: `rustup target add wasm32-wasip2`
- Zed must be restarted after installing Rust (GUI app doesn't inherit shell PATH)

## Resources

### Official Documentation
- [Zed Extensions Guide](https://zed.dev/docs/extensions/developing-extensions)
- [Zed Languages](https://zed.dev/docs/extensions/languages)
- [Zed Extension API Crate](https://crates.io/crates/zed_extension_api)
- [Tree-sitter Grammar Guide](https://tree-sitter.github.io/tree-sitter/creating-parsers)

### Language References
- [LSL Wiki](https://wiki.secondlife.com/wiki/LSL)
  - [LSL Functions](https://wiki.secondlife.com/wiki/Category:LSL_Functions)
- [OpenSimulator OSSL](https://opensimulator.org/wiki/Category:OSSL)
  - [OSSL Functions](http://opensimulator.org/wiki/Category:OSSL_Functions)
