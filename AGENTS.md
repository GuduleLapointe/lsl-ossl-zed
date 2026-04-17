# Agents instructions

## Project Overview

This is a **Zed IDE extension** providing language support for **LSL (Linden Scripting Language)** and **OSSL (OpenSimulator Scripting Language)**. The extension uses tree-sitter for parsing and provides syntax highlighting, structural analysis, and language intelligence for Second Life/OpenSimulator scripting.

## Project Structure

```
lsl-ossl-for-zed-ide/
├── Cargo.toml                    # Rust project configuration (Zed extension API)
├── extension.toml               # Zed extension metadata
├── languages/lsl-ossl/          # Tree-sitter language implementation
│   ├── config.toml             # Language configuration
│   ├── grammar.js              # Tree-sitter grammar definition
│   └── highlights.scm          # Syntax highlighting rules
├── tests/                      # Test files for both LSL and OSSL
│   ├── test.lsl               # LSL example script
│   └── test.ossl              # OSSL example script
├── snippets/                   # Code snippets (currently empty)
├── themes/                     # Custom themes (currently empty)
└── queries/                   # Tree-sitter query files (currently empty)
```

## Essential Commands

### Building
- **Build extension**: `cargo build` (requires Rust toolchain)
- **Development build**: Use Zed's extension development workflow
- **Testing**: Manual testing via test files in `tests/` directory

### Language Support Files
- **Grammar**: `languages/lsl-ossl/grammar.js` - Tree-sitter grammar for parsing
- **Highlighting**: `languages/lsl-ossl/highlights.scm` - Syntax highlighting rules
- **Config**: `languages/lsl-ossl/config.toml` - Language configuration

## Language Architecture

### Supported Languages
- **LSL (.lsl)**: Linden Scripting Language for Second Life
- **OSSL (.ossl)**: OpenSimulator Scripting Language extensions

### Key Language Features
- **States**: `default` and custom state definitions
- **Events**: LSL events like `state_entry`, `touch_start`, `timer`, etc.
- **Control Flow**: `if`, `for`, `while` statements
- **Functions**: User-defined functions and built-in function calls
- **Variables**: Type declarations with LSL types (integer, float, string, key, vector, rotation, list)
- **Expressions**: Binary operations, assignments, type casting
- **Constants**: TRUE, FALSE, PI, NULL_KEY, ZERO_VECTOR, ZERO_ROTATION

### Function Recognition
- **LSL Built-ins**: Functions starting with `ll*` prefix (e.g., `llSay`, `llSetText`)
- **OSSL Functions**: Functions starting with `os*` prefix (e.g., `osTeleportAgent`)
- **User Functions**: Custom function definitions and calls

## Code Patterns and Conventions

### File Extensions
- `.lsl` - Linden Scripting Language files
- `.ossl` - OpenSimulator Scripting Language files

### Language Configuration
- **Line comments**: `//` (single-line only in current grammar)
- **Tab size**: 4 spaces
- **Hard tabs**: Enabled (true)

### Grammar Structure
The tree-sitter grammar follows these patterns:
- Statement-based parsing with `_statement` rule as the main entry point
- Expression precedence handling for binary operations
- Event handlers as special function definitions
- State definitions with optional identifiers
- Block-based code organization

## Development Workflow

### Adding New Language Features
1. **Grammar updates**: Modify `languages/lsl-ossl/grammar.js`
2. **Highlighting**: Update `languages/lsl-ossl/highlights.scm`
3. **Testing**: Add test cases in `tests/` directory
4. **Configuration**: Update `languages/lsl-ossl/config.toml` if needed

### Testing Approach
- Manual testing via provided test files
- Test files cover both LSL and OSSL syntax
- Real-world examples included for validation

## Important Gotchas

### Grammar Limitations
1. **Comments**: Only single-line comments (`//`) are currently supported
2. **String literals**: Basic string support with escape sequences
3. **No multi-line comments**: `/* */` syntax not implemented in current grammar
4. **Limited expression precedence**: Some complex expressions may need parentheses

### Language Specifics
1. **Type system**: Limited to LSL primitive types (no custom types)
2. **Event handlers**: Must follow LSL event naming conventions
3. **State jumps**: `jump` and `state` statements are supported
4. **Function calls**: Both built-in and user-defined functions supported

### Zed Extension Development
1. **Zed API**: Uses `zed_extension_api` crate v0.7.0
2. **Extension type**: Library extension (`cdylib` crate type)

## Resources and References

### Official Documentation
- [Zed Extensions Guide](https://zed.dev/docs/extensions/developing-extensions)
- [Zed Languages](https://zed.dev/docs/extensions/languages)
- [Zed Extension API Crate](https://crates.io/crates/zed_extension_api)

### Tree-sitter Resources
- [Tree-sitter Grammar Guide](https://tree-sitter.github.io/tree-sitter/creating-parsers)
- [Tree-sitter Query Language](https://tree-sitter.github.io/tree-sitter/using-parsers#query-syntax)

### Language References
- [LSL Wiki](https://wiki.secondlife.com/wiki/LSL)
	- [LSL Functions](https://wiki.secondlife.com/wiki/Category:LSL_Functions)
- [OpenSimulator OSSL](https://opensimulator.org/wiki/Category:OSSL)
	- [OSSL Functions](http://opensimulator.org/wiki/Category:OSSL_Functions)

## Contributing

1. Fork the repository
2. Follow the development workflow above
3. Test changes with provided test files
4. Submit pull requests to the main repository
5. Follow the existing code patterns and conventions
