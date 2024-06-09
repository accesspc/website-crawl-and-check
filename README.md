# Website Crawl and Check

A website crawl and check is a little app that crawls the website for internal links and then keeps a status track of them

## Config file

Before running locally, make sure config file exist:

* config/config.yml

If not, create from sample file included in the repo:

* config/config.sample.yml

## Develop and run locally using virtual environment

```bash
# Setup
python3 -m venv .pyenv

# Activate
. .pyenv/bin/activate

# Install pip requirements
pip3 install -r requirements.txt

# Copy `config` to app dir
mkdir -p app/{config}
cp -fv config/config.yml app/config/

# Run
cd app
APP_DEBUG=TRUE python3 app.py

# Deactivate
deactivate
```

## Build and run locally on docker

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
