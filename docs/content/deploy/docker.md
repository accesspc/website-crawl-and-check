# Docker

## Configuration / config.yml

Before deploying, you need to create a configuration / config.yml file, that will be used to configure the application.

## Deploy

```bash
docker run -d -p 8000:8000 \
 -v $PWD/config/config.yml:/config/config.yml \
 accesspc/website-crawl-and-check:3.0.0
```
