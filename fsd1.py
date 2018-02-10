import requests
from time import sleep

url = "https://api.telegram.org/bot511531562:AAF8KDn_-CETUMNobPkatunhbVbIGHouy-g/" #url нашего бота

def get_updates_json(request):                              #обновления за 24 часа
    resp = requests.get(request + 'getUpdates')
    return resp.json()

def last_update(data):                                      #последнее обновление
    results = data['result']
    total_updates = len(results) - 1
    return results[total_updates]

def get_chatid(update):                                     #получение чат айди
    chat_id = update['message']['chat']['id']
    return chat_id

def send_msg(chat, txt):                                    #отправка сообщения ботом!
    params = {'chat: ': chat, 'text: ': txt}
    resp = requests.post(url + 'sendMessage', data=params)
    return resp

def main():
    update_id = last_update(get_updates_json(url))['update_id']
    while True:
        if update_id == last_update(get_updates_json(url))['update_id']:
            send_msg(get_chatid(last_update(get_updates_json(url))), 'test')
            update_id += 1
        sleep(1)

if __name__ == '__main__':
    main()



