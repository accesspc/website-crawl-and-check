# Prometheus configuration for metrics

Add the following section to `prometheus.yml`. Replace `192.168.68.32:30800` with your WCAC metrics endpoint IP/Hostname and port. Adjust `scheme` if it is running on `HTTPS`:

```yaml
scrape_configs:
  - job_name: wcac

    scheme: http

    static_configs:
      - targets:
          - 192.168.68.32:30800
```
