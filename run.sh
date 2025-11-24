#!/bin/bash
set -e

cd "$(dirname "$0")"

echo "Building backend image..."
docker build -t healthcare-backend .

echo "Restarting backend container..."
docker rm -f healthcare-backend 2>/dev/null || true

docker run -d \
  --name healthcare-backend \
  -p 8000:8000 \
  healthcare-backend

echo "Backend running at http://localhost:8000"