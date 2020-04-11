import telebot


class TelegramBot(object):
    def __init__(self, token, target_id):
        self.target_id = target_id

        self._handler = telebot.TeleBot(token)

    def send(self, data):
        # FIXME error while Markdown enabled
        """
        [b'{"ok":false,"error_code":400,"description":"Bad Request: can\'t parse entities: Can\'t find end of the entity starting at byte offset 31"}']
        """

        return self._handler.send_message(
            self.target_id,
            f'{data}',
            # parse_mode='Markdown'
        )
