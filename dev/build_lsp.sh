#!/bin/bash
# Build LSP prebuilt binaries for all supported platforms.
#
# On macOS  : builds both Mac arches natively, merges with lipo, then
#             cross-compiles Linux and Windows with cargo-zigbuild.
# On Linux  : builds Linux targets natively, Windows with cargo-zigbuild.
#             macOS targets require macOS and are skipped.
# On Windows: builds Windows targets natively, Linux with cargo-zigbuild.
#             macOS targets require macOS and are skipped.
#
# Prerequisites:
#   cargo install cargo-zigbuild
#   brew install zig      # macOS
#   apt install zig       # Debian/Ubuntu
#   scoop install zig     # Windows
#
# Usage: ./dev/build_lsp.sh

set -e
cd "$(dirname "$0")/.."

PREBUILT="lsp/prebuilt"
MANIFEST="lsp/Cargo.toml"
mkdir -p "$PREBUILT"

# --- Prerequisite checks ---

if ! command -v cargo &>/dev/null; then
    echo "❌ cargo not found — install Rust: https://rustup.rs"
    exit 1
fi

if ! command -v zig &>/dev/null; then
    echo "❌ zig not found — needed for cross-compilation"
    echo "   macOS : brew install zig"
    echo "   Linux : apt install zig  (or download from ziglang.org)"
    echo "   Windows: scoop install zig"
    exit 1
fi

if ! cargo zigbuild --version &>/dev/null 2>&1; then
    echo "❌ cargo-zigbuild not found — run: cargo install cargo-zigbuild"
    exit 1
fi

# --- Detect host OS ---

case "$(uname -s 2>/dev/null || echo Windows)" in
    Darwin)  HOST_OS="macos" ;;
    Linux)   HOST_OS="linux" ;;
    *)       HOST_OS="windows" ;;
esac

echo "==> Building LSP (host: $HOST_OS)"
echo ""

# --- Helper functions ---

native() {
    local rust_target="$1" out="$2"
    echo "  [$rust_target] native"
    rustup target add "$rust_target" --quiet
    cargo build --manifest-path "$MANIFEST" --release --target "$rust_target" --quiet
    local bin="lsp/target/${rust_target}/release/lsl-lsp"
    [[ "$rust_target" == *windows* ]] && bin="${bin}.exe"
    cp "$bin" "$PREBUILT/$out"
    echo "  ✅ $out"
}

zigbuild() {
    local rust_target="$1" out="$2"
    echo "  [$rust_target] cargo-zigbuild"
    rustup target add "$rust_target" --quiet
    cargo zigbuild --manifest-path "$MANIFEST" --release --target "$rust_target" --quiet
    local bin="lsp/target/${rust_target}/release/lsl-lsp"
    [[ "$rust_target" == *windows* ]] && bin="${bin}.exe"
    cp "$bin" "$PREBUILT/$out"
    echo "  ✅ $out"
}

# --- macOS universal binary ---

if [ "$HOST_OS" = "macos" ]; then
    echo "==> macOS (universal fat binary)"
    rustup target add aarch64-apple-darwin x86_64-apple-darwin --quiet
    cargo build --manifest-path "$MANIFEST" --release \
        --target aarch64-apple-darwin --quiet
    cargo build --manifest-path "$MANIFEST" --release \
        --target x86_64-apple-darwin --quiet
    lipo -create -output "$PREBUILT/lsl-lsp-macos" \
        lsp/target/aarch64-apple-darwin/release/lsl-lsp \
        lsp/target/x86_64-apple-darwin/release/lsl-lsp
    echo "  ✅ lsl-lsp-macos (universal: aarch64 + x86_64)"
    echo ""
else
    echo "  ⚠️  macOS targets skipped (require macOS SDK)"
    echo ""
fi

# --- Linux ---

echo "==> Linux"
if [ "$HOST_OS" = "linux" ]; then
    native x86_64-unknown-linux-gnu  lsl-lsp-linux-x86_64
    native aarch64-unknown-linux-gnu lsl-lsp-linux-aarch64
else
    zigbuild x86_64-unknown-linux-gnu  lsl-lsp-linux-x86_64
    zigbuild aarch64-unknown-linux-gnu lsl-lsp-linux-aarch64
fi
echo ""

# --- Windows ---

echo "==> Windows"
if [ "$HOST_OS" = "windows" ]; then
    native x86_64-pc-windows-msvc lsl-lsp-windows-x86_64.exe
else
    zigbuild x86_64-pc-windows-gnu lsl-lsp-windows-x86_64.exe
fi
echo ""

# --- Summary ---

echo "Prebuilt binaries:"
ls -lh "$PREBUILT/"
