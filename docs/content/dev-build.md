# Development

## Run locally using python virtual environment

Allows for quick and interactive development.

```bash
# Setup
python3 -m venv .pyenv

# Activate
. .pyenv/bin/activate

# Install pip requirements
pip install -r requirements.txt

# Copy `config` to app dir
mkdir -p app/{config}
cp -fv config/config.yml app/config/

# Run
cd app
APP_DEBUG=TRUE python3 app.py

# Deactivate
deactivate
```

Open app with URL: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
