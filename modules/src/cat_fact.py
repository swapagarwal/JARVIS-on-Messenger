import requests
import json
import config
import modules
from templates.quick_replies import add_quick_reply
from templates.text import TextTemplate


def process(input, entities=None):
    output = {}
    try:
        url = "https://catfact.ninja/fact"
        response = requests.get(url)
        data = response.json()
        cat_fact = data['fact']
        message = add_quick_reply(message, 'Another fact!', modules.generate_postback('cat_fact'))
        output['input'] = input
        output['output'] = message
        output['success'] = True
    except:
        output['success'] = False
    return output
