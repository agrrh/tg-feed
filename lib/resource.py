import requests
import uuid

from bs4 import BeautifulSoup
from urllib.parse import urljoin

from lib.target import Target


class Resource(object):
    # TODO parametrize? use some secret?
    # Random UUID to preserve consistent namespace
    __uuid = uuid.UUID('urn:uuid:886313e1-3b8a-5372-9b90-0c9aee199e5d')

    def __init__(self, **kwargs):
        self.url = kwargs.get('url')
        self.target = Target(kwargs.get('target'))

    @property
    def uuid(self):
        return str(uuid.uuid5(self.__uuid, self.url))

    def __prettify(self, piece):
        if not piece.url.startswith('http://'):
            piece.url = urljoin(self.url, piece.url)

        if piece.text:
            piece.text = piece.text.strip()

        return piece

    def get(self):
        try:
            resp = requests.get(self.url)
        except Exception:
            return False

        if resp.status_code == requests.codes.ok:
            return BeautifulSoup(resp.content, 'html.parser')

        return False

    def parse(self, content):
        return [
            self.__prettify(piece)
            for piece
            in self.target.find(content)
        ]
