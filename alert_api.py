from flask import Flask, request
import telebot, json, time

bot = telebot.TeleBot("5382490304:AAHAVgrcmrKFoSx2pNrjVpsAYF8aeQlz-Bc")
app = Flask(__name__)

@app.route('/')
def index():
    return 'Server on'

@app.route('/alert/<chatid>', methods=['GET','POST'])
def alert(chatid):
    try:
        if request.method == 'POST':
            data = request.get_json()
            json_data = json.loads(data)
            alert = json_data["alert"]
        elif request.method == 'GET':
            alert = request.args.get('alert')
        bot.send_message(chatid, alert)
        return "ok"
    except Exception as e:
        return e

app.run()