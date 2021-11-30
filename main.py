import telebot
from utilidades.utilidades import moeda

CHAVE_API = "2130502582:AAGBpiQc382sfWvsGXU0EjYWX-YKbo62JvI"

bot = telebot.TeleBot(CHAVE_API, threaded=False)
bot.remove_webhook()
bot.set_webhook(url=f' https://nfthunterbot.herokuapp.com/{CHAVE_API}')

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


bot.polling()
