from lib.config import Config
from lib.service import Service
from lib.state import State

# Init Config
config = Config()

# Init State
state = State()

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
