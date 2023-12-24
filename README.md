# Website Crawl and Check

A website crawl and check is a little app that crawls the website for internal links and then keeps a status track of them

## Config and State files

Before running locally, make sure these files exist:

* config.yml
* state.json

If not, create from sample files included in the repo:

* config.sample.yml
* state.sample.json

## Build and run locally

```bash
docker compose up website-check --build
```

## Build and push Docker hub

Login to Docker hub, if not already done so:

```bash
docker login [registry-1.docker.io]
```

Build and push to Docker hub:

```bash
docker build -t accesspc/website-crawl-and-check:v1.0.0 .
docker push accesspc/website-crawl-and-check:v1.0.0
```
