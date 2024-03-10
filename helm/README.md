# Deploy in K8s using Helm

A few notes:

* `wcac` - K8s namespace
* `app` - name used for helm release

## Configuration / values.yaml

Before deploying, you need to create a configuration / values.yaml file, that will be used to deploy the app.

## Install

```bash
helm install \
  -f values.yml \
  --create-namespace \
  --namespace wcac \
  app \
  website-crawl-and-check
```

### Upgrade

```bash
helm upgrade \
  -f values.yml \
  --namespace wcac \
  app \
  website-crawl-and-check
```

## Uninstall

```bash
helm uninstall --namespace wcac app
```
