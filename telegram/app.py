import telebot, requests, json, time, random, string, os

bot = telebot.TeleBot(os.sys.argv[1])
url = os.sys.argv[2]
tokens = {}

def newToken(size):
    random.seed(time.time())
    return ''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k = size))

@bot.message_handler(commands=['newToken'])
def send_new_token(message):
    token = newToken(12)
    response = requests.get(url + 'newToken?' + 'token=' + token + '&chatId=' + str(message.chat.id))
    if response and response.text == 'token active':
        tokens[message.chat.id] = token
        bot.reply_to(message, 'new token:')
        bot.send_message(message.chat.id, token)
    else:
        bot.reply_to(message, 'internal error')

@bot.message_handler(commands=['seen'])
def send_welcome(message):
    requests.get(url + 'setSeen?token=' + tokens[message.chat.id])

@bot.message_handler(commands=['help'])
def send_welcome(message):
	bot.reply_to(message,'''
/newToken - to get your chat token
/seen - confirm recived''')


if __name__ == '__main__':
   bot.infinity_polling()

