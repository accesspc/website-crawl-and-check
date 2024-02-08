# Deploy in K8s

FYI: `wcac` - is the short version of website-crawl-and-check

## Pre-requisites

For the CronJob to be able to mount a PersistentVolume from NFS, k8s workers must have an `nfs-common` package installed:

```bash
apt install nfs-common -y
```

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
