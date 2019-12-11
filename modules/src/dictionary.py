import os

import requests
import requests_cache

import config
from templates.text import TextTemplate

WORDS_API_KEY = os.environ.get('WORDS_API_KEY', config.WORDS_API_KEY)
URBANDICTIONARY_API_KEY = os.environ.get('URBANDICTIONARY_KEY', config.URBANDICTIONARY_API_KEY)


def urban_definition(input, entities):
    word = entities['word'][0]['value']
    urban_querystring = {"term": word}
    urban_url = "https://mashape-community-urban-dictionary.p.rapidapi.com/define"
    urban_headers = {
        'x-rapidapi-host': "mashape-community-urban-dictionary.p.rapidapi.com",
        'x-rapidapi-key': URBANDICTIONARY_API_KEY
    }

    response = requests.request("GET", urban_url, headers=urban_headers, params=urban_querystring)
    urban_data = response.json()

    urban_def = (urban_data['list'][0]['definition']).replace('[','').replace(']','')
    thumbs_up = urban_data['list'][0]['thumbs_up']
    thumbs_down = urban_data['list'][0]['thumbs_down']

    definition = "Urban Dictionary definition of " + word + ':\n'
    definition += urban_def + "\nThumbs Up: " + str(thumbs_up)
    definition += "\nThumbs Down: " + str(thumbs_down)

    return definition


def process(input, entities):
    output = {}
    try:
        word = entities['word'][0]['value']

        with requests_cache.enabled('dictionary_cache', backend='sqlite', expire_after=86400):
            r = requests.get('https://wordsapiv1.p.mashape.com/words/' + word + '/definitions', headers={
                'X-Mashape-Key': WORDS_API_KEY
            })
            data = r.json()
        def1 = 'Definition of ' + word + ':\n' + data['definitions'][0]['definition']

        try:
            def2 = urban_definition(input, entities)
            print('after urban')
        except:
            def2 = ''

        if len(def2) == 0:
            output['output'] = TextTemplate(def1).get_message()
        else:
            output['output'] = TextTemplate(def1 + '\n\n' + def2).get_message()

        output['input'] = input
        output['success'] = True
    except:
        try:
            def2 = urban_definition(input, entities)
        except:
            def2 = ''

        if len(def2) != 0:
            output['output'] = TextTemplate(def2).get_message()
            output['input'] = input
            output['success'] = True
        else:
            error_message = 'I couldn\'t find that definition.'
            error_message += '\nPlease ask me something else, like:'
            error_message += '\n  - define comfort'
            error_message += '\n  - cloud definition'
            error_message += '\n  - what does an accolade mean?'
            output['error_msg'] = TextTemplate(error_message).get_message()
            output['success'] = False

    return output
