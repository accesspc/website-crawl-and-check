from flask import Flask
from flask_apscheduler import APScheduler

from lib.config import Config
from lib.service import Service
from lib.state import State

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
        service = Service(web)

        if 'crawl' in web.keys():
            if web['crawl']:
                print('Crawl is not implemented yet')
            else:
                print('Crawl is disabled, will check for pages')
        
        if 'pages' in web.keys():
            for page in web['pages']:
                url = ''.join([web['url'], page])

                check = service.check(url)
                print(check)

                if url not in state.states:
                    check['status'] = 'init'
                
                state.states[url] = check['status']

    state.save()

if __name__ == "__main__":
    app.run(debug=True)
