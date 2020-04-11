from itertools import zip_longest

from lib.piece import Piece


class Target(object):
    def __init__(self, target_config):
        if isinstance(target_config, str):
            self.url_selector = target_config
        elif isinstance(target_config, dict):
            self.url_selector = target_config.get('url')
            self.text_selector = target_config.get('text')
        else:
            raise Exception(f'Wrong target config: {target_config}')

    def find(self, content):
        url_list = []
        text_list = []

        url_list = [
            found.get('href')
            for found
            in content.select(self.url_selector)
        ]

        if hasattr(self, 'text_selector'):
            text_list = [
                found.text
                for found
                in content.select(self.text_selector)
            ]

        for url, text in zip_longest(url_list, text_list):
            yield Piece(url, text)
