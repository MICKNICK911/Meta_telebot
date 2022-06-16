import requests
import json
import utils
import config
import time
import telebot
from telebot import types

message_id = []
chat_id = []
pre_chat = []
kill_reply = []
bye = []
trash = ['open']
warning = []

while True:
    try:
        current_user_info = {}
        answer = True
        same_user = False
        print(utils.get_user_info(current_user_info))

        if current_user_info["message_id"] in bye:
            print(bye)
            pass

        elif current_user_info['name'] in warning and current_user_info['text'] in warning:
            pass

        else:
            warning.clear()
            print('passing')
            text = str(current_user_info["text"]).lower()

            if current_user_info["chat_id"] in chat_id:
                same_user = True

                if not pre_chat:
                    pre_chat.clear()
                    pre_chat.append(current_user_info["chat_id"])

            else:
                chat_id.clear()
                chat_id.append(current_user_info["chat_id"])

                if not pre_chat:
                    pre_chat.clear()
                    pre_chat.append(current_user_info["chat_id"])

            if current_user_info["chat_id"] != pre_chat[0]:
                trash.clear()
                trash.append("engaged")

            if current_user_info["message_id"] in message_id or current_user_info["chat_id"] != pre_chat[0] or trash[
                0] == "engaged":
                answer = False

            else:
                message_id.clear()
                message_id.append(current_user_info["message_id"])

            print('asking')
            if answer:
                print('answer')
                if same_user:
                    print('same user')
                    if kill_reply:
                        utils.delete_chat(current_user_info["chat_id"], kill_reply[0])
                        kill_reply.clear()

                    if "bye" in text:
                        bot_reply = utils.reply("Thanks for chatting", current_user_info["chat_id"])
                        pre_chat.clear()
                        chat_id.clear()
                        message_id.clear()
                        kill_reply.clear()
                        bye.clear()
                        bye.append(current_user_info["message_id"])
                        trash.clear()
                        trash.append('open')

                    else:
                        print('reply')
                        bot_reply = utils.reply("I am alive", current_user_info["chat_id"])

                        print(bot_reply)
                        kill_reply.append(bot_reply)

                    utils.delete_chat(current_user_info["chat_id"], current_user_info["message_id"])

                else:
                    print('reply')
                    bot_reply = utils.reply("I am alive", current_user_info["chat_id"])

                    print(bot_reply)
                    kill_reply.append(bot_reply)

                    utils.delete_chat(current_user_info["chat_id"], current_user_info["message_id"])
                # utils.delete_chat(current_user_info["chat_id"], bot_reply)

            else:
                if pre_chat:
                    if pre_chat[0] != current_user_info["chat_id"]:
                        utils.delete_chat(current_user_info["chat_id"], current_user_info["message_id"])
                        bot_reply = utils.reply(f"Please {current_user_info['name']}\nI will be with you shortly",
                                                current_user_info["chat_id"])
                        print(bot_reply)
                        time.sleep(2)
                        utils.delete_chat(current_user_info["chat_id"], bot_reply)
                        warning.append(current_user_info['name'])
                        warning.append(current_user_info['text'])

                        trash.clear()
                        trash.append('open')


    except:
        pass
    time.sleep(0.1)
