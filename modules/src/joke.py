import json
import requests
from random import randrange

import config
import modules
from templates.quick_replies import add_quick_reply
from templates.text import TextTemplate


def download_new_joke(joke_idx, jokes):
    r = requests.get('https://icanhazdadjoke.com/', headers={'Accept': 'application/json'})
    resp = r.json()
    tick = 0
    while 'joke' in resp and tick <= 10:
        if resp['joke'] not in jokes['jokes']+jokes['used_jokes']:
            return resp['joke']
        else:
            resp = requests.get('https://icanhazdadjoke.com/', headers={'Accept': 'application/json'}).json()
            tick += 1
    else:
        return ''


def process(input, entities=None):
    output = {}
    try:
        with open(config.JOKES_SOURCE_FILE) as jokes_file:
            jokes = json.load(jokes_file)
        jokes_list = jokes['jokes']
        joke_idx = randrange(len(jokes_list))
        joke = jokes_list[joke_idx]
        message = TextTemplate(joke).get_message()
        message = add_quick_reply(message, 'One more!', modules.generate_postback('joke'))
        message = add_quick_reply(message, 'Show me a quote.', modules.generate_postback('quote'))
        message = add_quick_reply(message, 'Tell me a fact.', modules.generate_postback('fact'))
        if 'used_jokes' not in jokes:
            jokes['used_jokes'] = []
        jokes['used_jokes'].append(joke)
        new_joke = download_new_joke(joke_idx, jokes)
        if new_joke:
            print(new_joke)
            jokes_list[joke_idx] = new_joke
        output['input'] = input
        output['output'] = message
        output['success'] = True
        with open(config.JOKES_SOURCE_FILE, 'w') as jokes_file:
            jokes_file.write(json.dumps(jokes, indent=2))
    except:
        output['success'] = False
    return output
