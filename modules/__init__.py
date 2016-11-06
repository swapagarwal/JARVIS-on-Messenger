import config
import json
import os
import requests
import sys
from src import *
from templates.text import TextTemplate

WIT_AI_ACCESS_TOKEN = os.environ.get('WIT_AI_ACCESS_TOKEN', config.WIT_AI_ACCESS_TOKEN)

def process_query(input):
    try:
        r = requests.get('https://api.wit.ai/message?v=20160420&q=' + input, headers={
            'Authorization': 'Bearer %s' % WIT_AI_ACCESS_TOKEN
        })
        data = r.json()
        intent = data['outcomes'][0]['intent']
        entities = data['outcomes'][0]['entities']
        confidence = data['outcomes'][0]['confidence']
        if intent in src.__all__ and confidence > 0.5:
            return intent, entities
        else:
            return None, {}
    except:
        return None, {}

def search(input, sender=None, postback=False):
    if postback:
        payload = json.loads(input)
        intent = payload['intent']
        entities = payload['entities']
    else:
        intent, entities = process_query(input)
    if intent is not None:
        if intent in src.__personalized__ and sender is not None:
            r = requests.get('https://graph.facebook.com/v2.6/' + str(sender), params={
                'fields': 'first_name',
                'access_token' : os.environ.get('ACCESS_TOKEN', config.ACCESS_TOKEN)
            })
            entities['sender'] = r.json()
        data = sys.modules['modules.src.' + intent].process(input, entities)
        if data['success']:
            return data['output']
        else:
            if 'error_msg' in data:
                return data['error_msg']
            else:
                return TextTemplate('Something didn\'t work as expected! I\'ll report this to my master.').get_message()
    else:
        return TextTemplate('I\'m sorry; I\'m not sure I understand what you\'re trying to say sir.\nTry typing "help" or "request"').get_message()
