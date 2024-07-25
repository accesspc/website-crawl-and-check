import logging
import requests

log = logging.getLogger('crawl')

class Service():

    state = {}

    # Init
    def __init__(self) -> None:

        self._expected_code = 200
        self._headers = {}
        self._id = ''
        self._path = ''
        self._proto = 'https'
        self._proxies = {}
        self._timeout = 5
        self._url = ''

        self.session = requests.Session()

    # Attributes
    ## Expected code
    @property
    def expected_code(self):
        return self._expected_code

    @expected_code.setter
    def expected_code(self, value):
        if isinstance(value, int) and value >= 100 and value <= 599:
            self._expected_code = value
        else:
            log.error('expected_code must be integer in the range of [100, 599]')

    ## Headers
    @property
    def headers(self):
        return self._headers

    @headers.setter
    def headers(self, value):
        if isinstance(value, dict):
            self._headers = value
        else:
            log.error('headers must be a dict of key: value pairs')

    ## ID
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    ## Path
    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, value):
        self._path = value
        self._url = f'{self._proto}://{self._id}{self._path}'

    ## Proto
    @property
    def proto(self):
        return self._proto

    @proto.setter
    def proto(self, value):
        if value in ('http', 'https'):
            self._proto = value
        else:
            log.error('proto must be either http or https')

    ## Proxies
    @property
    def proxies(self):
        return self._proxies

    @proxies.setter
    def proxies(self, value):
        if isinstance(value, dict):
            self._proxies = value
        else:
            log.error('proxies must be a dict of key: value pairs')

    ## Timeout
    @property
    def timeout(self):
        return self._timeout

    @timeout.setter
    def timeout(self, value):
        if isinstance(value, (int, float)) and value > 0 and value <= 60:
            self._timeout = value
        else:
            log.error('timeout value must be float between 0 and 60')

    ## URL
    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value

    # Check page
    def check(self) -> None:

        # Perform get request
        response = self.request_get()

        # Build a state dict
        self.state = {
            'proto': self._proto,
            'id': self._id,
            'path': self._path,
            'code': response.status_code,
            'size': len(response.text),
            'time': response.elapsed.total_seconds(),
        }

        log.info(self.state)

    # get states
    def get_state(self) -> tuple:
        return self._url, self.state

    # requests.get
    def request_get(self) -> object:

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

        except requests.exceptions.HTTPError as ex:
            log.error(f'Http Error: {ex}')
            log.error(self.url)
        except requests.exceptions.ConnectionError as ex:
            log.error(f'Error Connecting: {ex}')
        except requests.exceptions._timeout as ex:
            log.error(f'Timeout Error: {ex}')
        except requests.exceptions.RequestException as ex:
            log.error(f'OOps: Something Else {ex}')
        return False

    # requests.post
    def request_post(self, data={}, json={}) -> object:

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

        except requests.exceptions.HTTPError as ex:
            log.error(f'Http Error: {ex}')
        except requests.exceptions.ConnectionError as ex:
            log.error(f'Error Connecting: {ex}')
        except requests.exceptions._timeout as ex:
            log.error(f'Timeout Error: {ex}')
        except requests.exceptions.RequestException as ex:
            log.error(f'OOps: Something Else: {ex}')
        return False
