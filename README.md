# Website Crawl and Check

A website crawl and check is a little app that crawls the website for internal links and then keeps a status track of them

## Config and State files

Before running locally, make sure these files exist:

* config/config.yml
* state/state.json

If not, create from sample files included in the repo:

* config/config.sample.yml
* state/state.sample.json

## Dev and run locally using virtual environment

```bash
# Setup
python3 -m venv .venv

# Activate
. .venv/bin/activate

# Install pip requirements
pip3 install -r requirements.txt

# Copy `config` and `state` to app dir
mkdir -p app/{config,state}
cp -fv config/config.yml app/config/
cp -fv state/state.json app/state/

# Run
cd app
python3 app.py

# Deactivate
deactivate
```

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
