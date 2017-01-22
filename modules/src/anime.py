import requests
import requests_cache
from templates.button import *

def process(input, entities):
    output = {}
    try:
        anime = entities['anime'][0]['value']

        with requests_cache.enabled('anime_cache', backend='sqlite', expire_after=86400):
            r = requests.get('https://hummingbird.me/api/v1/search/anime', params={
                'query': anime
            })
            data = r.json()

        template = TextTemplate()
        template.set_text('Title: ' + data[0]['title'] + '\nSynopsis: ' + data[0]['synopsis'])
        template.set_post_text('\nCommunity Rating: ' + str(round(data[0]['community_rating'], 2)) + ' / 5' + '\nStatus: ' + data[0]['status'])
        text = template.get_text()

        template = ButtonTemplate(text)
        template.add_web_url('Hummingbird URL', data[0]['url'])

        output['input'] = input
        output['output'] = template.get_message()
        output['success'] = True
    except:
        error_message = 'I couldn\'t find any anime matching your query.'
        error_message += '\nPlease ask me something else, like:'
        error_message += '\n  - Death Note anime'
        error_message += '\n  - Dragon ball super anime status'
        error_message += '\n  - What is the anime rating of One Punch Man?'
        output['error_msg'] = TextTemplate(error_message).get_message()
        output['success'] = False
    return output
