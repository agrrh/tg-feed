import hashlib
import requests

from bs4 import BeautifulSoup
from urllib.parse import urljoin

from lib.entity import Entity

# FIXME comments


class Resource(object):
    def __init__(self, **kwargs):
        self.url = kwargs.get('url')
        self.entities = [
            Entity(e)
            for e
            in kwargs.get('entities', [])
        ]

        self.hash = self.__hash_get()

    def __hash_get(self):
        return hashlib.md5(self.url.encode()).hexdigest()

    def __data_process(self, data):
        for url in data:
            if isinstance(url, str):
                if not url.startswith('http://'):
                    url = urljoin(self.url, url)
                yield (url, None)

            if isinstance(url, tuple):
                url, content = url
                if not url.startswith('http://'):
                    url = urljoin(self.url, url)
                yield (url, content)

    # TODO use some database (sqlite?)
    def last_update(self, data):
        with open(f'./data/{self.hash}.dat', 'w+') as fp:
            fp.write(data)

    # TODO use some database (sqlite?)
    @property
    def last(self):
        try:
            with open(f'./data/{self.hash}.dat', 'r') as fp:
                return fp.read()
        except FileNotFoundError:
            return None

    @property
    def entities_list(self):
        return [
            self.__data_process(entity.data)
            for entity
            in self.entities
        ]

    def parse(self):
        try:
            resp = requests.get(self.url)
        except requests.exceptions.ConnectionError:
            return None

        if resp.status_code == requests.codes.ok:
            html = BeautifulSoup(resp.content, 'html.parser')

            [
                entity_instance.parse(html)
                for entity_instance
                in self.entities
            ]
