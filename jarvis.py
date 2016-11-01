import config
from flask import Flask, request
import json
import os
import requests
import modules

ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN', config.ACCESS_TOKEN)
VERIFY_TOKEN = os.environ.get('VERIFY_TOKEN', config.VERIFY_TOKEN)

MARK_SEEN = 0
SEND_TYPING_ON = 1
SEND_TYPING_OFF = 2

app = Flask(__name__)

@app.route('/')
def about():
    return 'Just A Rather Very Intelligent System, now on Messenger!'

@app.route('/process/')
def process():
    return json.dumps(modules.process_query(request.args.get('q')))

@app.route('/search/')
def search():
    return json.dumps(modules.search(request.args.get('q')))
    
def senderaction(senderid, actiontype):
    if actiontype == MARK_SEEN:
        action = 'mark_seen'
    elif actiontype == SEND_TYPING_ON:
        action = 'typing_on'
    else :
        action = 'typing_off'
    payload = {
        'recipient': {
            'id': senderid
        },
        'sender_action': action
    }
    r = requests.post('https://graph.facebook.com/v2.6/me/messages', params={'access_token': ACCESS_TOKEN}, json=payload)
    return 'Done'

@app.route('/webhook/', methods=['GET', 'POST'])
def webhook():
    if request.method == 'POST':
        data = request.get_json(force=True)
        messaging_events = data['entry'][0]['messaging']
        for event in messaging_events:
            sender = event['sender']['id']
            senderaction(sender, MARK_SEEN)
            if 'message' in event and 'text' in event['message']:
                text = event['message']['text']
                senderaction(sender, SEND_TYPING_ON)
                payload = {
                    'recipient': {
                        'id': sender
                    },
                    'message': modules.search(text)
                }
                r = requests.post('https://graph.facebook.com/v2.6/me/messages', params={'access_token': ACCESS_TOKEN}, json=payload)
            if 'postback' in event and 'payload' in event['postback']:
                postback = event['postback']['payload']
                payload = {
                    'recipient': {
                        'id': sender
                    },
                    'message': modules.search(postback, postback=True)
                }
                r = requests.post('https://graph.facebook.com/v2.6/me/messages', params={'access_token': ACCESS_TOKEN}, json=payload)
        return ''  # 200 OK
    elif request.method == 'GET':  # Verification
        if request.args.get('hub.verify_token') == VERIFY_TOKEN:
            return request.args.get('hub.challenge')
        else:
            return 'Error, wrong validation token'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=True)
