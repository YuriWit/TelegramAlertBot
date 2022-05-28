from flask import Flask, request
import telebot, json

bot = telebot.TeleBot("5382490304:AAHAVgrcmrKFoSx2pNrjVpsAYF8aeQlz-Bc")
app = Flask(__name__)
seen = {}

@app.route('/')
def index():
    return 'Server on'

@app.route('/alert/<chatid>', methods=['GET','POST'])
def alert(chatid):
    try:
        seen[chatid] = False
        if request.method == 'POST':
            data = request.get_json()
            json_data = json.loads(data)
            alert = json_data["alert"]
        elif request.method == 'GET':
            alert = request.args.get('alert')
        else:
            raise Exception('Method not suported')
        bot.send_message(chatid, alert + "\n/seen")
        return "ok"
    except Exception as e:
        return str(e)

@app.route('/seen/<chatid>', methods=['GET','POST'])
def chech(chatid):
    try:
        if request.method == 'POST':
            data = request.get_json()
            json_data = json.loads(data)
            chat_seen = json_data["seen"]
            seen[chatid] = chat_seen
            return "ok"
        elif request.method == 'GET':
            return str(seen[chatid])
        else:
            raise Exception('Method not suported')
    except Exception as e:
        return str(e)

app.run(port=80)
