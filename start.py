import requests
import datetime
import logging


logger = logging.getLogger(__name__)

token = '695762397:AAGm5DuunnPYmLDeeshF12C0igEOHQFCk9w'


class BotHandler:
    def __init__(self, token):
        self.token = token
        self.api_url = "https://api.telegram.org/bot" + token + "/"

    def get_updates(self, offset=None, timeout=30):
        method = 'getUpdates'
        params = {'timeout': timeout, 'offset': offset}
        resp = requests.get(self.api_url + method, params)
        print(resp.json())
        print(self.api_url + method)
        result_json = (resp.json())['result']
        print(result_json)
        return result_json

    def send_message(self, chat_id, text):
        params = {'chat_id': chat_id, 'text': text}
        method = 'sendMessage'
        resp = requests.post(self.api_url + method, params)
        print(1)
        return resp

    def get_last_update(self):
        get_result = self.get_updates()

        if len(get_result) > 0:
            last_update = get_result[-1]
        else:
            return 0

        return last_update


def main():
    greet_bot = BotHandler(token)

    new_offset = None

    while True:
        greet_bot.get_updates(new_offset)

        last_update = greet_bot.get_last_update()

        if last_update != 0:
            last_update_id = last_update['update_id']
            last_chat_text = last_update['message']['text']
            last_chat_id = last_update['message']['chat']['id']
            # last_chat_name = last_update['message']['chat']['first_name']

            greet_bot.send_message(last_chat_id, 'sosi{}'.format(last_chat_text))

            new_offset = last_update_id + 1


if __name__ == '__main__':
    main()
