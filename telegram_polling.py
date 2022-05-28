import telebot
import requests, json

bot = telebot.TeleBot("5382490304:AAHAVgrcmrKFoSx2pNrjVpsAYF8aeQlz-Bc")
url = "http://127.0.0.1/seen/"
data = json.dumps({"seen": True})

@bot.message_handler(commands=['getid'])
def send_welcome(message):
    bot.reply_to(message, "chat id: " + str(message.chat.id))

@bot.message_handler(commands=['seen'])
def send_welcome(message):
    requests.post(url + str(message.chat.id), json=data)

@bot.message_handler(commands=['help'])
def send_welcome(message):
	bot.reply_to(message,"""
/getid - to get your chat id
/seen - confirm recived""")

bot.infinity_polling()