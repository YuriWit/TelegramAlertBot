from flask import Flask, request
import telebot, json, time

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
        for i in range(10):
            bot.send_message(chatid, alert)
            time.sleep(1)
        return "ok"
    except Exception as e:
        return e

app.run()