import requests
from urllib.parse import quote, urlencode, urljoin


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

    def get_source_metadata(self, module_id, url, options=None):
        query = (
            ('options', options),
        )
        request_url = self._make_url('sources/metadata/%s/%s' % (module_id, quote(url, safe='')), query)
        return requests.get(request_url).json()

    def list_sources(self, group_id=0, recursive=False, auto_download_media=None, persist_thumbnails=None, error=None):
        query = (
            ('group_id', group_id),
            ('recursive', recursive),
            ('auto_download_media', auto_download_media),
            ('persist_thumbnails', persist_thumbnails),
            ('error', error),
        )
        request_url = self._make_url('sources', query)
        return requests.get(request_url).json()['sources']

    def get_source(self, module_id, id):
        request_url = self._make_url('sources/%s/%s' % (module_id, id))
        return requests.get(request_url).json()

    def add_source(self, module_id, url, id=None, group_id=None, options=None, name=None, thumbnail_url=None, web_url=None, auto_download_media=None, persist_thumbnails=None):
        request_url = self._make_url('sources')
        return requests.post(request_url, json={
            'module_id': module_id,
            'url': url,
            'id': id,
            'group_id': group_id,
            'options': options,
            'name': name,
            'thumbnail_url': thumbnail_url,
            'web_url': web_url,
            'auto_download_media': auto_download_media,
            'persist_thumbnails': persist_thumbnails,
        }).json()

    def edit_source(self, module_id, id, group_id=0, url=None, options=None, name=None, thumbnail_url=None, web_url=None, auto_download_media=None, persist_thumbnails=None):
        request_url = self._make_url('sources/%s/%s' % (module_id, id))
        return requests.post(request_url, json={
            'group_id': group_id,
            'url': url,
            'options': options,
            'name': name,
            'thumbnail_url': thumbnail_url,
            'web_url': web_url,
            'auto_download_media': auto_download_media,
            'persist_thumbnails': persist_thumbnails,
        }).json()

    def remove_source(self, module_id, id):
        request_url = self._make_url('sources/%s/%s' % (module_id, id))
        return requests.delete(request_url).json()

    def update_source(self, module_id, id, viewed=False):
        request_url = self._make_url('sources/%s/%s/update' % (module_id, id))
        return requests.post(request_url, json={
            'viewed': viewed,
        }).json()
