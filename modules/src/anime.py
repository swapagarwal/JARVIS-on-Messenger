import requests
import requests_cache
from templates.button import *
from error_msg import QUERY_ERROR, EXAMPLE_ANIME

def process(input, entities):
    output = {}
    try:
        anime = entities['anime'][0]['value']

        with requests_cache.enabled('anime_cache', backend='sqlite', expire_after=86400):
            r = requests.get('https://kitsu.io/api/edge/anime', params={
                'filter[text]': anime
            })
            data = r.json()

        top_anime = data['data'][0]['attributes']

        template = TextTemplate()
        template.set_text('Title: ' + top_anime['canonicalTitle'] + '\nSynopsis: ' + top_anime['synopsis'])
        template.set_post_text('\nAverage Rating: ' + top_anime['averageRating'] + '%')
        text = template.get_text()

        template = ButtonTemplate(text)
        template.add_web_url('Kitsu URL', 'https://kitsu.io/anime/' + top_anime['slug'])

        output['input'] = input
        output['output'] = template.get_message()
        output['success'] = True
    except:
        error_message = QUERY_ERROR.format('anime') + EXAMPLE_ANIME
        output['error_msg'] = TextTemplate(error_message).get_message()
        output['success'] = False
    return output
