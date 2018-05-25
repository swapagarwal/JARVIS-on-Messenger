import json
import os
import sys

import keen
import requests

import config
import modules
from src import *
from templates.quick_replies import add_quick_reply
from templates.text import TextTemplate

WIT_AI_ACCESS_TOKEN = os.environ.get('WIT_AI_ACCESS_TOKEN', config.WIT_AI_ACCESS_TOKEN)


def generate_postback(module):
    return {
        'intent': module,
        'entities': None
    }


def process_query(input):
    # For local testing, mock the response from Wit
    with open(config.WIT_LOCAL_DATA) as wit_file:
        wit_local_data = json.load(wit_file)
        if input.lower() in wit_local_data:
            return wit_local_data[input.lower()]['intent'], wit_local_data[input.lower()]['entities']
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
    # TODO: Needs to be refactored out
    try:
        keen.project_id = os.environ.get('KEEN_PROJECT_ID', config.KEEN_PROJECT_ID)
        keen.write_key = os.environ.get('KEEN_WRITE_KEY', config.KEEN_WRITE_KEY)
        keen.add_event('logs', {
            'intent': intent,
            'entities': entities,
            'input': input,
            'sender': sender,
            'postback': postback
        })
    except:
        pass  # Could not stream data for analytics
    if intent is not None:
        if intent in src.__personalized__ and sender is not None:
            r = requests.get('https://graph.facebook.com/v2.6/' + str(sender), params={
                'fields': 'first_name',
                'access_token': os.environ.get('ACCESS_TOKEN', config.ACCESS_TOKEN)
            })
            if entities is None:
                entities = {}
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
        message = TextTemplate(
            'I\'m sorry; I\'m not sure I understand what you\'re trying to say.\nTry typing "help" or "request"').get_message()
        message = add_quick_reply(message, 'Help', modules.generate_postback('help'))
        message = add_quick_reply(message, 'Request', modules.generate_postback('request'))
        return message
