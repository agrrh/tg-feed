from lib.resource import Resource


class ResourceManager(object):
    def __init__(self, storage=None, resource_config=None):
        self.storage = storage
        self.resource = Resource(**resource_config)

    @property
    def checkpoint(self):
        return self.storage.get(self.resource.uuid)

    def check_resource(self):
        content = self.resource.get()

        if not content:
            return False

        return self.resource.parse(content)

    def select_news(self, resource_pieces):
        if resource_pieces and not self.checkpoint:
            yield resource_pieces[0]

        for piece in resource_pieces:
            if piece.hash == self.checkpoint:
                break

            yield piece

    def notify(self, telegram, news_list):
        checkpoint_saved = False

        for piece in news_list:
            if not checkpoint_saved:
                self.storage.put(
                    self.resource.uuid,
                    piece.hash
                )
                checkpoint_saved = True

            # If text is separated due to being too long
            if isinstance(piece.pretty, list):
                for pretty_part in piece.pretty:
                    telegram.send(pretty_part)
            else:
                telegram.send(piece.pretty)
