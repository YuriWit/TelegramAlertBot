from flask import Flask, request
import telebot, json

bot = telebot.TeleBot("5382490304:AAHAVgrcmrKFoSx2pNrjVpsAYF8aeQlz-Bc")
app = Flask(__name__)

@app.route('/')
def index():
    return 'Server on'

@app.route('/alert/<chatid>', methods=['POST'])
def alert(chatid):
    try:
        data = request.get_json()
        json_data = json.loads(data)
        alert = json_data["alert"]
        bot.send_message(chatid, alert)
        return "ok"
    except Exception as e:
        return e

app.run()