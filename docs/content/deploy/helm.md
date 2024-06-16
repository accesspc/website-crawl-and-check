# Helm

## Configuration / values.yaml

Before deploying, you need to create a configuration / values.yaml file, that will be used to deploy the app.

## Install / Upgrade

```bash
helm upgrade --install \
  -f values.yml \
  --namespace wcac \
  app \
  website-crawl-and-check
```

## Uninstall

```bash
helm uninstall --namespace wcac app
```
