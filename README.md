# Tree-sitter LSL / OSSL

A Tree-sitter grammar for **LSL (Linden Scripting Language)** and **OSSL (OpenSimulator Scripting Language)**.

This project enables syntax highlighting and basic structural parsing for LSL/OSSL in Tree-sitter compatible editors such as Zed and Neovim.

- Syntax highlighting for LSL/OSSL
- Recognition of native `ll*` functions
- Recognition of OSSL `os*` functions
- Support for LSL events
- Native constants and types support
- A Tree-sitter compatible grammar foundation

## Supported languages
- LSL (Second Life / OpenSim)
- OSSL (OpenSimulator extensions)

### Language coverage
- Variables
- User-defined functions
- States (`default`, `state`)
- Events (`state_entry`, `touch_start`, etc.)
- Control flow (`if`, `for`, `while`)
- Expressions and function calls
- Type casting `(integer)`, `(string)`, etc.

### Automatic recognition
- LSL native functions: `llSay`, `llSetText`, etc.
- OSSL functions: `osTeleportAgent`, etc.
- Constants: `TRUE`, `FALSE`, `PI`, `NULL_KEY`, etc.

### Supported File Extensions

- `.lsl` - Linden Scripting Language files
- `.ossl` - OpenSimulator Scripting Language files

## License

See the [LICENSE](LICENSE) file for details.
