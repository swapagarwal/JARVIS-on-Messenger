import requests
import json
import config
import modules
from templates.quick_replies import add_quick_reply
from templates.text import TextTemplate


def process(input, entities=None):
    output = {}
    try:
        url = "https://www.boredapi.com/api/activity"
        response = requests.get(url)
        data = response.json()
        message = data['activity']
        message = add_quick_reply(message, 'Something else!', modules.generate_postback('bored'))
        output['input'] = input
        output['output'] = message
        output['success'] = True
    except:
        output['success'] = False
    return output
