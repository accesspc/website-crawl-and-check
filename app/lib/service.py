import logging
import requests

from datetime import datetime

log = logging.getLogger('crawl')

class Service():

    states = {}

    # Init
    def __init__(self) -> None:
        self._base = ''
        self._expected_code = 200
        self._headers = {}
        self._path = ''
        self._proxies = {}
        self._timeout = 5
        self._url = ''

        self.session = requests.Session()
    
    # Attributes
    ## Base
    @property
    def base(self):
        return self._base
    
    @base.setter
    def base(self, value):
        self._base = value
    
    ## Expected code
    @property
    def expected_code(self):
        return self._expected_code
    
    @expected_code.setter
    def expected_code(self, value):
        if isinstance(value, int) and value >= 100 and value <= 599:
            self._expected_code = value
        else:
            log.error(f'expected_code must be integer in the range of [100, 599]')

    ## Headers
    @property
    def headers(self):
        return self._headers
    
    @headers.setter
    def headers(self, value):
        self._headers = value
    
    ## Path
    @property
    def path(self):
        return self._path
    
    @path.setter
    def path(self, value):
        self._path = value
    
    ## Proxies
    @property
    def proxies(self):
        return self._proxies
    
    @proxies.setter
    def proxies(self, value):
        self._proxies = value
    
    ## Timeout
    @property
    def timeout(self):
        return self._timeout
    
    @timeout.setter
    def timeout(self, value):
        if isinstance(value, (int, float)) and value > 0 and value <= 60:
            self._timeout = value
        else:
            log.error(f'timeout value must be float between 0 and 60')
    
    ## URL
    @property
    def url(self):
        return self._url
    
    @url.setter
    def url(self, value):
        self._url = value
    
    # Check page
    def check(self) -> None:

        self._url = ''.join([
            self._base,
            self._path
        ])

        response = self.requestGet()

        state = {
            'code': response.status_code,
            'size': len(response.text),
            'time': response.elapsed.total_seconds(),
        }

        self.states[self._path] = state

        log.info({
            'url': self._base,
            'path': self._path,
            'state': state,
        })

    # get states
    def getStates(self) -> dict:
        return self.states

    # requests.get
    def requestGet(self) -> object:
        try:

            request = self.session.get(
                self.url,
                headers=self._headers,
                proxies=self._proxies,
                timeout=self._timeout
            )

            if request.status_code != self._expected_code:
                log.error(
                    f'HTTP response: {request.status_code}: {request.reason}')
                return False

            return request

        except requests.exceptions.HTTPError as errh:
            log.error('Http Error:', errh)
            log.error(self.url)
        except requests.exceptions.ConnectionError as errc:
            log.error('Error Connecting:', errc)
        except requests.exceptions._timeout as errt:
            log.error('Timeout Error:', errt)
        except requests.exceptions.RequestException as err:
            log.error('OOps: Something Else', err)
        return False

    # requests.post
    def requestPost(self, data={}, json={}) -> object:
        try:

            request = self.session.post(
                self.url,
                data=data,
                json=json,
                headers=self._headers,
                proxies=self._proxies,
                timeout=self._timeout
            )

            if request.status_code != self.request_status_code:
                log.error(
                    f'HTTP response: {request.status_code}: {request.reason}')
                return False

            return request

        except requests.exceptions.HTTPError as errh:
            log.error('Http Error:', errh)
        except requests.exceptions.ConnectionError as errc:
            log.error('Error Connecting:', errc)
        except requests.exceptions._timeout as errt:
            log.error('Timeout Error:', errt)
        except requests.exceptions.RequestException as err:
            log.error('OOps: Something Else', err)
        return False
