# Deploy in K8s

FYI: `wcac` - is the short version of website-crawl-and-check

## Namespace

```bash
kubectl apply -f k8s/namespace.yml
```

## App

```bash
# ConfigMap: preview
kubectl kustomize config/

# Apply
kubectl apply -k config/
kubectl apply -f k8s/
```
