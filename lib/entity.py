# FIXME bad naming
# FIXME comments


class Entity(object):
    def __init__(self, definition):
        if isinstance(definition, str):
            self.patterns = {
                'url': definition
            }
        elif isinstance(definition, dict):
            self.patterns = {
                'url': definition.get('url'),
                'content': definition.get('content')
            }
        else:
            raise Exception('NoPatterns')

        self.data = []

    def parse(self, html):
        url_list = [
            html_url.get('href')
            for html_url
            in html.select(self.patterns.get('url'))
        ]

        self.data = url_list

        if self.patterns.get('content'):
            content_list = [
                html_content.text.strip()[:135]
                for html_content
                in html.select(self.patterns.get('content'))
            ]

            self.data = zip(url_list, content_list)
