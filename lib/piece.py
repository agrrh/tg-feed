import hashlib


class Piece(object):
    def __init__(self, url, text):
        self.url = url
        self.text = text

    @property
    def hash(self):
        return hashlib.md5(self.url.encode()).hexdigest()

    @property
    def pretty(self):
        pretty = f'{self.url}'

        # TODO limit too long texts
        if self.text:
            pretty = f'{self.url}\n\n{self.text}'

        return pretty
