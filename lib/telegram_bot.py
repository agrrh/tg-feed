import logging
import telebot
import time


class TelegramBot(object):
    def __init__(self, token, target_id):
        self.target_id = target_id

        self._handler = telebot.TeleBot(token)

    def __send(self, data):
        # FIXME error while Markdown enabled
        """
        [b'{"ok":false,"error_code":400,"description":"Bad Request: can\'t parse entities: Can\'t find end of the entity starting at byte offset 31"}']
        """
        # self._handler.send_message(
        #     self.target_id,
        #     f'{data}',
        #     parse_mode='Markdown'
        # )

        try:
            self._handler.send_message(
                self.target_id,
                f'{data}',
            )
        except telebot.apihelper.ApiException as e:
            msg, method_name, result = e
            logging.error(f'Error sending message: {e}')
            return result.json(), False

        # response, success
        return True, True

    def send(self, data):
        result, success = None, False

        while not success:
            result, success = self.__send(data)

            logging.debug(f'Tried to send message: success: {success}; result: {result}')

            if isinstance(result, dict) and result.get('ok'):
                break

            if isinstance(result, dict) and 'retry_after' in result.get('parameters', {}):
                retry_after = result.get('parameters', {}).get('retry_after', 20)
                logging.warning(f'Would retry after {retry_after} seconds')
                time.sleep(retry_after)
