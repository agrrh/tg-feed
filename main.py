import yaml
import telebot

from lib.resource import Resource


if __name__ == '__main__':
    with open('./config.yml') as fp:
        config = yaml.load(fp, Loader=yaml.SafeLoader)

    telegram = telebot.TeleBot(
        config.get('telegram').get('token')
    )

    # TODO threading
    for resource_config in config.get('resources'):
        resource = Resource(**resource_config)
        resource.parse()

        # FIXME notifies only for latest entry
        for entity in resource.entities_list:
            for entity_data in entity:
                url, content = entity_data

                if url == resource.last:
                    break

                telegram.send_message(
                    config.get('telegram').get('chat_id'),
                    f"{url}",
                    parse_mode='Markdown'
                )

                resource.last_update(url)
                break
