import requests
import requests_cache
from templates.button import *

KITSU_URL = 'https://kitsu.io/anime/'

def process(input, entities):
    output = {}
    try:
        anime = entities['anime'][0]['value']
        with requests_cache.enabled('anime_cache', backend='sqlite', expire_after=86400):
            r = requests.get('https://kitsu.io/api/edge/anime', params={
                'filter[text]': anime
            })
            data = r.json()

        top_result = data['data'][0]
        english_title = top_result['attributes']['titles']['en']
        synopsis = top_result['attributes']['synopsis']
        avg_rating = top_result['attributes']['averageRating']

        template = TextTemplate()
        template.set_text('Title: ' + english_title + '\nSynopsis: ' + synopsis)
        template.set_post_text('\nCommunity Rating: ' + str(round(avg_rating, 2)) + ' / 5')
        text = template.get_text()

        template = ButtonTemplate(text)
        template.add_web_url('Kitsu URL', KITSU_URL + top_result['attributes']['slug'])

        output['input'] = input
        output['output'] = template.get_message()
        output['success'] = True
    except:
        error_message = 'I couldn\'t find any anime matching your query.'
        error_message += '\nPlease ask me something else, like:'
        error_message += '\n  - Death Note anime'
        error_message += '\n  - What is the anime rating of One Punch Man?'
        output['error_msg'] = TextTemplate(error_message).get_message()
        output['success'] = False
    return output
