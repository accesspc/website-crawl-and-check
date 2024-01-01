# Deploy in K8s

FYI: `wcac` - is the short version of website-crawl-and-check

## Pre-requisites

For the CronJob to be able to mount a PersistentVolume from NFS, k8s workers must have an `nfs-common` package installed:

```bash
apt install nfs-common -y
```

## Namespace

```bash
kubectl create namespace wcac
```

## ConfigMap

```bash
# Create
kubectl -n wcac create configmap wcac-config --from-file=config.yml

# Verify
kubectl -n wcac get configmap wcc-config
kubectl -n wcac describe configmap wcc-config
```

## PersistantVolume

```bash
# Create
kubectl apply -f k8s/pv.yml

# Verify
kubectl get pv bl1-nfs-vol
kubectl describe pv bl1-nfs-vol
```

## PersistantVolumeClaim

```bash
# Create
kubectl apply -f k8s/pvc.yml

# Verify
kubectl -n wcac get pvc nfs-pvc
kubectl -n wcac describe pvc nfs-pvc
```

## CronJob

```bash
# Create / update
kubectl apply -f k8s/cronjob.yml

# Verify
kubectl -n wcac get cronjobs
kubectl -n wcac get pods

# Logs (dirty way)
kubectl -n wcac logs $(kubectl -n wcac get pods | tail -1 | cut -d' ' -f1)
```
