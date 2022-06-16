import requests
import json
import config


def get_user_info(determiner: dict):
    info = f'https://api.telegram.org/bot{config.SECRET_KEY}/getUpdates'
    retrieve = requests.get(info)
    content = retrieve.__dict__
    a = content['_content']

    out = json.loads(a.decode('utf-8'))
    print(out)
    output = out['result'][-1]

    determiner["chat_id"] = output['message']['from']['id']
    determiner["message_id"] = output['message']["message_id"]

    out1 = output['message']['from']["first_name"]
    out2 = output['message']['from']["last_name"]
    determiner["name"] = f"{out1} {out2}"

    determiner["text"] = output["message"]["text"]
    return determiner


def reply(msg: str, chat_id):
    base_url = f'https://api.telegram.org/bot{config.SECRET_KEY}/sendMessage?chat_id={chat_id}&text=*{msg}*&parse_mode=markdown'
    retrieve = requests.get(base_url)
    content = retrieve.__dict__
    a = content['_content']

    out = json.loads(a.decode('utf-8'))
    print(out)
    return out["result"]["message_id"]


def delete_chat(chat_id, message_id):
    reset_url = f'https://api.telegram.org/bot{config.SECRET_KEY}/deleteMessage?chat_id={chat_id}&message_id={message_id}'
    requests.get(reset_url)
    print("Successful_bot")
