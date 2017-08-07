import requests
from urllib.parse import urlencode, urljoin


class Server(object):
    def __init__(self, addr):
        self._addr = addr

    def _make_url(self, path, query=[]):
        request_url = urljoin(self._addr, path)
        query = urlencode([(k, v) for k, v in query if v is not None])
        if query:
            request_url = '%s?%s' % (request_url, query)
        return request_url

    def list_modules(self, url=None, options=None):
        query = (
            ('url', url),
            ('options', options),
        )
        request_url = self._make_url('modules', query)
        return requests.get(request_url).json()['modules']

    def get_module(self, id):
        request_url = self._make_url('modules/%s' % id)
        return requests.get(request_url).json()
