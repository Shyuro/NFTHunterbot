import telebot
from utilidades.utilidades import moeda
import os
from flask import Flask, request


PORT = int(os.environ.get('PORT', 5000))
CHAVE_API = "2130502582:AAGBpiQc382sfWvsGXU0EjYWX-YKbo62JvI"
server = Flask(__name__)

bot = telebot.TeleBot(CHAVE_API, threaded=False)
global crypto_list
crypto_list = ['BNB', 'ROFI', 'USDT']


def verificar(mensagem):
    global msg
    if str(mensagem.text).upper() in crypto_list:
        msg = str(mensagem.text).upper()
        return True


@bot.message_handler(func=verificar)
def responder(mensagem):
    global msg
    bot.send_message(mensagem.chat.id, moeda(f'{msg}'))


@bot.message_handler(commands=['add'])
def adicionar(mensagem):
    new_token = str(mensagem.text).replace('/add ', '')
    new_token = new_token.upper()
    crypto_list.append(new_token)


@server.route('/' + CHAVE_API, methods=['POST'])
def getMessage():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200


@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://nfthunterbot.herokuapp.com/' + CHAVE_API)
    return "!", 200


if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
