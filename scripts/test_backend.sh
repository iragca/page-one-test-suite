#/bin/bash

docker compose -f docker_backend/docker-compose.yml up --build -d

uv run pytest docker_backend/test_backend.py

docker compose -f docker_backend/docker-compose.yml down
