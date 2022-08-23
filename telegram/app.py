import telebot
import requests, json

def newToken(size):
    random.seed(time.time())
    return ''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k = size))

bot = telebot.TeleBot('5382490304:AAHAVgrcmrKFoSx2pNrjVpsAYF8aeQlz-Bc')
url = 'http://localhost/'
tokens = {}

@bot.message_handler(commands=['newToken'])
def send_new_token(message):
    token = newToken(16)
    response = requests.get(url + 'newToken?' + 'token=' + token + '&chatId=' + str(message.chat.id))
    if response and response.text == 'token active':
        tokens[message.chat.id] = token
        bot.reply_to(message, 'new token: ' + token)
    else:
        bot.reply_to(message, 'internal error')

@bot.message_handler(commands=['seen'])
def send_welcome(message):
    requests.get(url + 'setSeen?' + tokens[message.chat.id])

@bot.message_handler(commands=['help'])
def send_welcome(message):
	bot.reply_to(message,'''
/newToken - to get your chat token
/seen - confirm recived''')


if __name__ == '__main__':
   bot.infinity_polling()

