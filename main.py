import schedule
import sys
import time

from lib.config import Config
from lib.storage import Storage
from lib.resource_manager import ResourceManager
from lib.telegram_bot import TelegramBot


if __name__ == '__main__':
    config = Config('./config.yml')

    storage = Storage(config.storage)
    telegram = TelegramBot(
        config.telegram.get('token'),
        config.telegram.get('target_id'),
    )

    managers_list = [
        ResourceManager(
            storage=storage,
            resource_config=resource_config
        )
        for resource_config
        in config.resources
    ]

    def payload():
        # TODO proper logging
        print('Payload started')

        # TODO threading
        for resource_manager in managers_list:
            resource_pieces = resource_manager.check_resource()
            news = resource_manager.select_news(resource_pieces)
            resource_manager.notify(telegram, news)

        print('Payload finished')

    # TODO use argparse or fire
    if '--daemon' in sys.argv:
        print('Run in daemon mode')

        # First run is immediate
        payload()
        time.sleep(60)

        # Next runs are distributed in random 1-5 minutes intervals
        schedule.every(1).to(5).minutes.do(payload)

        while True:
            schedule.run_pending()
            time.sleep(1)
    else:
        print('Run in one-time mode')

        payload()
