import os

import requests
import requests_cache
import json

import config
from templates.text import TextTemplate



def process(input, entities):
    output = {}
    try:
        word = entities[0]['value']
        url = "http://api.urbandictionary.com/v0/define?term={0}".format(word)
        response = requests.get(url)
        if response.ok:
            output['input'] = input
            definition = json.loads(response.content)["list"][0]["definition"]
            output['output'] = TextTemplate(
                word.capitalize() + ": " + definition).get_message()
            output['success'] = True
        else:
            raise Exception("Urban dictionary definition not found.")
    except:
        error_message = 'I couldn\'t find the meaning of that word'
        output['error_msg'] = TextTemplate(error_message).get_message()
        output['success'] = False
    return output