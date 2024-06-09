# Deploy in K8s using Helm

A few notes:

* `wcac` - K8s namespace
* `app` - name used for helm release

## Configuration / values.yaml

Before deploying, you need to create a configuration / values.yaml file, that will be used to deploy the app.

## Linting

```bash
helm lint website-crawl-and-check
```

## Template debug

```bash
helm template wcac website-crawl-and-check -f values.yml --debug
```

## Package

```bash
helm package website-crawl-and-check
```

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
