#!/bin/bash
# Deploy grammar changes: generate parser, push grammar repo, update extension hash.
# Usage: ./deploy-grammar.sh ["commit message"]

set -e

cd "$(dirname "$0")"

MESSAGE="${1:-Update grammar}"

echo "==> Generating parser..."
(cd grammar && npm run build)

echo "==> Committing grammar repo..."
(cd grammar && git add -A && git commit -m "$MESSAGE" && git push)

echo "==> Updating grammar hash in extension.toml..."
HASH=$(git -C grammar rev-parse HEAD)
sed -i '' "s/commit = \".*\"/commit = \"$HASH\"/" extension.toml

echo "==> Committing extension repo..."
git add extension.toml grammar
git commit -m "Update grammar: $MESSAGE"

echo ""
echo "Done. Rebuild the extension in Zed to apply changes."
