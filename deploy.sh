#!/bin/bash
set -euo pipefail
cd "$(dirname "$0")"

if [[ ! -f node_modules/.bin/wrangler ]]; then
  npm install
fi

echo "Deploying Dominica site to dominica-shore-excursions worker..."
npx wrangler deploy

echo "Done. Check https://dominicashoreexcursions.com/ in a minute."
