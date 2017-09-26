import json
import os
import detect_drowsiness
import random
import emoji
from unidecode import unidecode

import requests
from flask import Flask, request

import config
import modules

ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN', config.ACCESS_TOKEN)
VERIFY_TOKEN = os.environ.get('VERIFY_TOKEN', config.VERIFY_TOKEN)

dict = {}

dict["'\U0001f604'"] = ['Good to see you happy', 'your laugh!!!', 'Happy faces are the best']
dict["'\U0001f600'"] = ['tell me what is that grin about?','Hahahah','you are funny']
dict["'\U0001f601'"] = ['Good to see you happy', 'this reaction lights up my day', 'Happy faces are the best']
dict["'\U0001f602'"] = ['glad you found it funny', 'you found it funny, pal?', 'i am also bursting into laughter']
dict["'\U0001f603'"] = ['Good to see you happy', 'Keep grinning', 'look at those eyes']
dict["'\U0001f606'"] = ['i think you are enjoying our conversation', 'what is so funny pal?', 'it is always to talk to you']
dict["'\U0001f609'"] = ['wink wink', 'hahahah...', 'buddy you are funny']
dict["'\U0001f60A'"] = ['Glad to be at your service', 'Keep grinning', 'and here is my favorite person again']#
dict["'\U0002f61A'"] = ['always keep smiling', 'happy to help', 'you seem to be in a good mood']#
dict["'\U0001f610'"] = ['Good to see you happy', 'glad to help', 'what can I do for you']#
dict["'\U0002f639'"] = ['you look unhappy', 'you look upset', 'what is wrong with you?']
dict["'\U0001f610'"] = ["what's up","buddy what do you want to talk about?","hey there, why are you so blank?"]
dict["'\U0001f611'"] = ['okay, say something',"what's up","hey there, why are you so blank?"]
dict["'\U0001f644'"] = ['did i say something stupid?', 'what made you roll your eyes','Did i miss something?']
dict["'\U0001f60F'"] = ['may i know the reason for this reaction?','what made you smirk?','okay! please me explain the issue']#
dict["'\U0001f623'"] = ['you look rather irritated','am i boring you?','looks like we are no more having a smooth conversation!!!']
dict["'\U0001f62E'"] = ['Preety amazing huh','it is wow indeed',"You didn't except this,right?"]#
dict["'\U0001f62A'"] = ['yawning huh?',"you need to take some sleep","why dont you take some rest?"]#
dict["'\U0001f62B'"] = ["why are so tired?","did you hsve a hectic day today?","you should take some rest"]#
dict["'\U0001f620'"] = ['wohh,you are in mad mood','someone is in a bad mood','do you want to share with me something?']
dict["'\U0001f615'"] = ['why are you confused?','is there any confusion','i think i did not gave an apt reply..kindly ask your doubt again']
dict["'\U0001f631'"] = ['dont be afraid buddy!!!','what is this fear about?','i am here pal,dont worry']
dict["'\U0001f62C'"] = ['hahah','what are you grinning?','i always have a good time with you!!!']#
dict["'\U0001f628'"] = ['you look worried about something','what is bugging you buddy','you can share with anything if you want to'] 
dict["'\U0001f62D'"] = ['what made you cry pal?','something terrible must have happened for you cry like this','dont cry buddy,talk to me']#
dict["'\U0001f61F'"] = ['dont worry,i am here','lets talk it out','trust me and tell me your problem']#
dict["'\U0001f61E'"] = ['trust me and tell me your problem','why are you so dissapointed?','Did i dissapoint you?']#
dict["'\U0001f641'"] = ['you look unhappy', 'what is that frown about?', 'what is wrong with you?']


app = Flask(__name__)


@app.route('/')
def about():
    return 'Just A Rather Very Intelligent System, now on Messenger!'


@app.route('/camera')
def run():

    detect_drowsiness.main()

    return 'cool play again'


@app.route('/process/')
def process():
    
    #x =  request.args.get('q').encode('unicode-escape')    # read emoji and convert it to its unicode
    
    #print dict[x][random.randint(0,len(dict[x])-1)]
    #print request.args.get('q').decode('unicode-escape')    # read unicode and convert it to its emoji
    return json.dumps(modules.process_query(request.args.get('q')))


@app.route('/search/')
def search():
    return json.dumps(modules.search(request.args.get('q')))


@app.route('/webhook/', methods=['GET', 'POST'])
def webhook():
    if request.method == 'POST':

        data = request.get_json(force=True)
        messaging_events = data['entry'][0]['messaging']
        for event in messaging_events:
            sender = event['sender']['id']
            message = None

            if(request.args.get('q').encode('unicode-escape') in dict):
                
                x = request.args.get('q').encode('unicode-escape')
                payload = {
                    'recipient': {
                        'id': sender
                    },
                    'message': dict[x][random.randint(0,len(dict[x])-1)]
                }
                r = requests.post('https://graph.facebook.com/v2.6/me/messages', params={'access_token': ACCESS_TOKEN},
                                  json=payload)
                return ''

            if 'message' in event and 'text' in event['message']:

                if 'quick_reply' in event['message'] and 'payload' in event['message']['quick_reply']:
                    quick_reply_payload = event['message']['quick_reply']['payload']
                    message = modules.search(quick_reply_payload, sender=sender, postback=True)
                else:
                    text = event['message']['text']
                    message = modules.search(text, sender=sender)
            if 'postback' in event and 'payload' in event['postback']:
                postback_payload = event['postback']['payload']
                message = modules.search(postback_payload, sender=sender, postback=True)
            if message is not None:
                payload = {
                    'recipient': {
                        'id': sender
                    },
                    'message': message
                }
                r = requests.post('https://graph.facebook.com/v2.6/me/messages', params={'access_token': ACCESS_TOKEN},
                                  json=payload)
        return ''  # 200 OK
    elif request.method == 'GET':  # Verification
        if request.args.get('hub.verify_token') == VERIFY_TOKEN:
            return request.args.get('hub.challenge')
        else:
            return 'Error, wrong validation token'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=True)
