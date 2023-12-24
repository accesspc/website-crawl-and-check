import requests


class Service():

    def __init__(self, web):
        self.headers = {}
        self.proxies = {}
        self.request_status_code = 200
        self.session = requests.Session()
        self.timeout = web['timeout'] if 'timeout' in web else 5
        self.token = None
        self.url = ''
    
    def check(self, url):
        check = {
            'code': 0,
            'status': 'error',
            'size': 0,
            'time': 0,
            'timestamp': '',
            'msg': 'ok',
            'url': url
        }

        self.url = url

        response = self.requestGet()

        check['code'] = response.status_code
        check['size'] = len(response.text)
        check['time'] = response.elapsed.total_seconds()

        if response.status_code == self.request_status_code:
            check['status'] = 'ok'
        else:
            check['mksg'] = 'Website check: HTTP Status Code missmatch'
        
        return check

    def requestGet(self):
        try:

            request = self.session.get(
                self.url,
                headers=self.headers,
                proxies=self.proxies,
                timeout=self.timeout
            )

            if request.status_code != self.request_status_code:
                print(
                    f'! HTTP response: {request.status_code}: {request.reason}')
                return False

            return request

        except requests.exceptions.HTTPError as errh:
            print('! Http Error:', errh)
        except requests.exceptions.ConnectionError as errc:
            print('! Error Connecting:', errc)
        except requests.exceptions.Timeout as errt:
            print('! Timeout Error:', errt)
        except requests.exceptions.RequestException as err:
            print('! OOps: Something Else', err)
        return False

    def requestPost(self, data={}, json={}):
        try:

            request = self.session.post(
                self.url,
                data=data,
                json=json,
                headers=self.headers,
                proxies=self.proxies,
                timeout=self.timeout
            )

            if request.status_code != self.request_status_code:
                print(
                    f'! HTTP response: {request.status_code}: {request.reason}')
                return False

            return request

        except requests.exceptions.HTTPError as errh:
            print('! Http Error:', errh)
        except requests.exceptions.ConnectionError as errc:
            print('! Error Connecting:', errc)
        except requests.exceptions.Timeout as errt:
            print('! Timeout Error:', errt)
        except requests.exceptions.RequestException as err:
            print('! OOps: Something Else', err)
        return False
