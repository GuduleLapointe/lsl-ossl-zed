# Developer Guide

Follow Zed documentation
- extensions: https://zed.dev/docs/extensions/developing-extensions
- languages: https://zed.dev/docs/extensions/languages
- crate: https://crates.io/crates/zed_extension_api

This extension provides the language and the language support for LSL and OSSL scripting languages.

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
