import config
from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/webhook/', methods=['GET', 'POST'])
def webhook():
    if request.method == 'POST':
        data = request.get_json(force=True)
        messaging_events = data['entry'][0]['messaging']
        for event in messaging_events:
            sender = event['sender']['id']
            if event['message'] and event['message']['text']:
                text = event['message']['text']
                payload = {
                    'recipient': {
                        'id': sender
                    },
                    'message': {
                        'text': text + 'At your service, sir.'
                    }
                }
                r = requests.post('https://graph.facebook.com/v2.6/me/messages/?access_token=' + config.ACCESS_TOKEN, json=payload)
        return ''  # 200 OK
    elif request.method == 'GET':  # Verification
        if request.args.get('hub.verify_token') == config.VERIFY_TOKEN:
            return request.args.get('hub.challenge')
        else:
            return 'Error, wrong validation token'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
