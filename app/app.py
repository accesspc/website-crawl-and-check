import logging
import os
import sys

from flask import Flask, render_template
from flask_apscheduler import APScheduler
from flask_wtf import CSRFProtect
from waitress import serve

from lib.config import Config
from lib.jsonformatter import JsonFormatter
from lib.service import Service
from lib.state import State

version = 'v3.0.0'

# Logger
log = logging.getLogger()
log.setLevel(logging.INFO)
sh = logging.StreamHandler(sys.stdout)
sh.setFormatter(JsonFormatter({
    '@timestamp': 'asctime',
    'level': 'levelname',
    'logger': 'name',
    'message': 'message',
}))
sh.setLevel(logging.INFO)
log.addHandler(sh)

# Init Config
config = Config()

# Init State
state = State()

# Create app
app = Flask(__name__)
csrf = CSRFProtect()
csrf.init_app(app)

# Create scheduler
scheduler = APScheduler()
scheduler.api_enabled = True
scheduler.init_app(app)
scheduler.start()

# Define routes
@app.route('/')
def route_home():
    return render_template('index.html', version=version)

@app.route('/metrics')
def route_metrics():
    return '\n'.join(state.get_metrics()), 200, {'Content-Type': 'text/plain; charset=utf-8'}

# Define scheduler job
@scheduler.task(
        'interval',
        id='crawl',
        seconds=config.cron['seconds'] or 15
)
def cron_job():

    # Loop config.websites
    for web in config.websites:
        # Init crawl
        service = Service()
        service.id = web['id']
        service.proto = web['proto']

        if 'timeout' in web.keys():
            service.timeout = web['timeout']

        if 'crawl' in web.keys() and web['crawl']:
            log.warn('Crawl is not implemented yet')

        if 'paths' in web.keys():
            for path in web['paths']:
                service.path = path

                service.check()

                u, s = service.get_state()
                state.set_state(u, s)

if __name__ == "__main__":
    if 'APP_DEBUG' in os.environ:
        app.run(debug=os.environ['APP_DEBUG'], host='127.0.0.1', port=8000)
    else:
        serve(app, host="0.0.0.0", port=8000)
