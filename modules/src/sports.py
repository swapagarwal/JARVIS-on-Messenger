import json
import os
import config
import requests
import requests_cache
from templates.text import TextTemplate

LIVESCORE_API_KEY = os.environ.get('LIVESCORE_API_KEY', config.LIVESCORE_API_KEY)

def process(input, entities):
    output = {}
    print("I made it to sports")
    output['input'] = input

    try:
        url = "https://livescore6.p.rapidapi.com/news/list"
        querystring = {"Category":"soccer"}
        headers = {
            'x-rapidapi-key': "a847312084msh8af501f6e7e7d04p1ec38djsn9cbd1a29f416",
            'x-rapidapi-host': "livescore6.p.rapidapi.com"
        }
        response = requests.request("GET", url, headers=headers, params=querystring)
        data = response.json()
        output['success'] = True
        message = str(data['arts'][0]['tit'])
        message += '\n'
        message += str(data['arts'][0]['des'])
        output['output'] = TextTemplate(message).get_message()
    except:
        error_message = '\nPlease ask me something else.'
        output['error_msg'] = TextTemplate(error_message).get_message()
        output['success'] = False
    return output