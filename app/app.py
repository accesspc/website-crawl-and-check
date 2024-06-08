import logging
import sys

from flask import Flask
from flask_apscheduler import APScheduler
from waitress import serve

from lib.config import Config
from lib.jsonformatter import JsonFormatter
from lib.service import Service
from lib.state import State


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

# Create scheduler
scheduler = APScheduler()
scheduler.api_enabled = True
scheduler.init_app(app)
scheduler.start()

# Define routes
@app.route('/')
def route_home():
    return '<h1>Website crawl and check</h1>'

@app.route('/metrics')
def route_metrics():
    return state.states

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
        service.base = web['url']

        if 'timeout' in web.keys():
            service.timeout = web['timeout']

        if 'crawl' in web.keys() and web['crawl']:
            log.warn('Crawl is not implemented yet')

        if 'paths' in web.keys():
            for path in web['paths']:
                service.path = path

                service.check()

        state.update(web['url'], service.getStates())

        state.save()

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000)
