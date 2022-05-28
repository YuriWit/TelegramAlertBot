import telebot

bot = telebot.TeleBot("5382490304:AAHAVgrcmrKFoSx2pNrjVpsAYF8aeQlz-Bc")

@bot.message_handler(commands=['getid'])
def send_welcome(message):
    bot.reply_to(message, "chat id:" + str(message.chat.id))

@bot.message_handler(commands=['help'])
def send_welcome(message):
	bot.reply_to(message,"/getid - to get your chat id")

bot.infinity_polling()