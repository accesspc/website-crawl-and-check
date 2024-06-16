# Helm

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
