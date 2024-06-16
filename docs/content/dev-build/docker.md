# Docker

## Build and run locally

```bash
docker compose up website-check --build
```

## Build and push to Docker hub

Login to Docker hub, if not already done so:

```bash
docker login [registry-1.docker.io]
```

Build and push to Docker hub:

```bash
# Prepare build instance
docker buildx create --use

# Build and push to docker hub
docker buildx build --platform=linux/amd64,linux/arm64 --push -t accesspc/website-crawl-and-check:v3.0.0 .
docker buildx build --platform=linux/amd64,linux/arm64 --push -t accesspc/website-crawl-and-check:latest .

# Stop and remove build instances
docker buildx stop
docker buildx rm
```
