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

    def list_groups(self, root_id=None, recursive=True):
        query = (
            ('root_id', root_id),
            ('recursive', recursive),
        )
        request_url = self._make_url('groups', query)
        return requests.get(request_url).json()['groups']

    def get_group(self, id):
        request_url = self._make_url('groups/%s' % id)
        return requests.get(request_url).json()

    def add_group(self, name, parent_id=None):
        request_url = self._make_url('groups')
        return requests.post(request_url, json={
            'name': name,
            'parent_id': parent_id,
        }).json()

    def edit_group(self, id, parent_id=0, name=None):
        request_url = self._make_url('groups/%s' % id)
        return requests.post(request_url, json={
            'parent_id': parent_id,
            'name': name,
        }).json()

    def remove_group(self, id):
        request_url = self._make_url('groups/%s' % id)
        return requests.delete(request_url).json()
