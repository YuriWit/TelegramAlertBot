from flask import Flask, request
import telebot, os

bot = telebot.TeleBot(os.sys.argv[1])
app = Flask(__name__)
data = {}

@app.route('/')
def index():
    return 'Server on'

@app.route('/newToken', methods=['GET'])
def newToken():
    try:
        if 'token' not in request.args:
            return 'missing token'
        token = request.args.get('token')
        if 'chatId' not in request.args:
            return 'missing chatId'
        chatId = request.args.get('chatId')
        data[token] = {'chatId':chatId, 'seen':True}
        return 'token active'
    except Exception as e:
        return str(e)

@app.route('/alert', methods=['GET'])
def sendAlert():
    try:
        if 'token' not in request.args:
            return 'missing token'
        token = request.args.get('token')
        if token not in data:
            return 'invalid token'
        if 'alert' not in request.args:
            return 'missing alert' 
        alert = request.args.get('alert')
        chatId = data[token]['chatId']
        data[token]['seen'] = False
        bot.send_message(chatId, alert)
        return 'alert sent'
    except Exception as e:
        return str(e)

@app.route('/seen', methods=['GET'])
def sendSeen():
    try:
        if 'token' not in request.args:
            return 'missing token'
        token = request.args.get('token')
        if token not in data:
            return 'invalid token'
        return str(data[token]['seen'])
    except Exception as e:
        return str(e)

@app.route('/setSeen', methods=['GET'])
def setSeen():
    try:
        if 'token' not in request.args:
            return 'error'
        token = request.args.get('token')
        if token not in data:
            return 'error'
        data[token]['seen'] = True
        return 'seen set'
    except Exception as e:
        return str(e)


if __name__ == '__main__':
   app.run(host='0.0.0.0', port=80)
   