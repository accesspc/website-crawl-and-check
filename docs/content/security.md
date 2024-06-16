# Security testing

There are multiple tools that can be used for security testing. Here's a few and how to run them (sorted alphabetically):

## bandit

```bash
docker run --rm -v $PWD:/src ghcr.io/pycqa/bandit/bandit -r /src
# or
docker compose up bandit
```

## checkov

```bash
docker run --rm -v $PWD:/src bridgecrew/checkov -d /src --quiet
# or
docker compose up checkov
```

## semgrep

```bash
docker run --rm -v $PWD:/src returntocorp/semgrep semgrep scan .
# or
docker compose up semgrep
```

## trivy

```bash
# config
docker run --rm -v $PWD:/src aquasec/trivy config /src
# or
docker compose up trivy-config

# filesystem
docker run --rm -v $PWD:/src aquasec/trivy filesystem /src
# or
docker compose up trivy-filesystem
```
