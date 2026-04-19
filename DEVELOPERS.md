# Developer Guide

Follow Zed documentation
- extensions: https://zed.dev/docs/extensions/developing-extensions
- languages: https://zed.dev/docs/extensions/languages
- crate: https://crates.io/crates/zed_extension_api

This extension provides the language and the language support for LSL and OSSL scripting languages.

## Environment setup

Install rust with rustup:
```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

## LSP build

The LSP server is a Rust binary distributed as prebuilt binaries for each platform in `lsp/prebuilt/`.

| Binary | Covers |
|---|---|
| `lsl-lsp-macos` | macOS universal fat binary (Intel + Apple Silicon) |
| `lsl-lsp-linux-x86_64` | Linux x86_64 |
| `lsl-lsp-linux-aarch64` | Linux ARM64 |
| `lsl-lsp-windows-x86_64.exe` | Windows x86_64 (+ ARM64 via emulation) |

Build all targets from your development machine:

```bash
./dev/build_lsp.sh
```

Prerequisites: `cargo install cargo-zigbuild` and `zig` in PATH (`brew install zig` / `apt install zig` / `scoop install zig`). macOS targets require macOS and are skipped automatically on other platforms.

## TODO

- **Complete function/event lists**: add all documented LSL functions and OSSL functions to `highlights.scm`, and all LSL events to `grammar/grammar.js`
- **Snippets**: add event handler snippets (`state_entry`, `touch_start`, etc.) in `snippets/` for autocomplete
- **Formatter**: investigate prettier or a custom formatter for LSL code formatting on save
- **LSP**: implement language server for diagnostics, signature help, go-to-definition

## Grammar workflow

The tree-sitter grammar lives in a separate repo ([tree-sitter-lsl-ossl](https://github.com/GuduleLapointe/tree-sitter-lsl-ossl)), included here as a git submodule at `grammar/`.

The grammar is fully generated from the OpenSimulator C# source. **Never edit `grammar/grammar.js` by hand** — edit the template instead (`grammar/src/grammar-template.js`).

### Three separate steps

**1. Generate reference docs** — pulls the OpenSim source and extracts function, constant, and event lists:

```bash
./dev/generate_ref_docs.py
```

Writes `doc/*.md` (human-readable reference) and `logs/generate_ref_docs.stats.json` (counts report, not committed).
Review the generated Markdown files to verify the content before proceeding.

**2. Build grammar** — generates `grammar/grammar.js` from the template and the doc files, then compiles the parser:

```bash
./dev/build_grammar.py
```

Writes `grammar/grammar.js` (generated), compiles `grammar/src/parser.c` via `npm run build`, and writes `logs/build_grammar.stats.json` (not committed).
Review `grammar/grammar.js` and confirm there are no build errors before deploying.

**3. Deploy** — commits and pushes the grammar submodule, updates the extension hash, bumps the patch version, commits, tags, and pushes the main repo:

```bash
./dev/deploy-grammar.sh
```

This step reads `dev/build_grammar.stats.json` to compose the grammar commit message automatically.

### Files

| File | Role |
|---|---|
| `grammar/src/grammar-template.js` | Human-editable template — edit this to change grammar structure |
| `grammar/grammar.js` | Generated — do not edit by hand |
| `logs/generate_ref_docs.stats.json` | Counts report from step 1 (gitignored) |
| `logs/build_grammar.stats.json` | Counts report from step 2, consumed by deploy (gitignored) |

### Cloning with the submodule

```bash
git clone --recurse-submodules https://github.com/GuduleLapointe/lsl-ossl-zed.git
# or, if already cloned:
git submodule update --init
```

Note: avoid `git submodule sync` as it may overwrite local URL overrides (e.g. a git+ssh URL).

## Grammar Details

### Supported Constructs
- States (`default`, `state`)
- Events (`state_entry`, `touch_start`, etc.)
- Control flow (`if`, `for`, `while`)
- Functions and function calls
- Variables and types
- LSL constants (`TRUE`, `FALSE`, `PI`, etc.)
- LSL native functions (`ll*` prefix)
- OSSL functions (`os*` prefix)

### File Types
The grammar supports both `.lsl` and `.ossl` extensions.

## Contributing

Contributions are welcome! Please open issues or pull requests on the [GitHub repository](https://github.com/GuduleLapointe/lsl-ossl-zed).
