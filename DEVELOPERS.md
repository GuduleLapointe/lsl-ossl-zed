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

## Grammar workflow

The tree-sitter grammar lives in a separate repo ([tree-sitter-lsl-ossl](https://github.com/GuduleLapointe/tree-sitter-lsl-ossl)), included here as a git submodule at `grammar/`.

When the grammar changes:

1. Edit `grammar/grammar.js`
2. Regenerate the C parser: `cd grammar && tree-sitter generate`
3. Commit and push in the grammar repo: `cd grammar && git add -A && git commit -m "..." && git push`
4. Update the commit hash in `extension.toml`:
   ```toml
   [grammars.lsl]
   repository = "https://github.com/GuduleLapointe/tree-sitter-lsl-ossl"
   commit = "<new-hash>"   # ← update this after each grammar push
   ```
5. Commit the submodule pointer and `extension.toml` in the extension repo

To clone this repo with its submodule:
```bash
git clone --recurse-submodules git@github.com:GuduleLapointe/lsl-ossl-zed.git
# or, if already cloned:
git submodule update --init
```

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
