import hashlib

from telebot import util


class Piece(object):
    TEXT_LIMIT = 3000

    def __init__(self, url, text):
        self.url = url
        self.text = text

    @property
    def hash(self):
        return hashlib.md5(self.url.encode()).hexdigest()

    @property
    def pretty(self):
        pretty = f'{self.url}'

        if self.text:
            if len(self.text) > self.TEXT_LIMIT:
                pretty = util.split_string(self.text, self.TEXT_LIMIT)
                pretty = [
                    f'{n + 1}/{len(pretty)} : {self.url}\n\n{portion}'
                    for n, portion
                    in enumerate(pretty)
                ]
            else:
                pretty = f'{self.url}\n\n{self.text}'

        return pretty
