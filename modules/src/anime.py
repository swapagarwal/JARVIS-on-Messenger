import requests
from templates.button import *

def process(input, entities):
    output = {}
    try:
        anime = entities['search_query'][0]['value']
        r = requests.get('https://hummingbird.me/api/v1/search/anime', params={
            'query': anime
        })
        data = r.json()

        template = TextTemplate()
        template.set_text('Title: ' + data[0]['title'] + '\nSynopsis: ' + data[0]['synopsis'])
        template.set_post_text('\nCommunity Rating: ' + str(round(data[0]['community_rating'], 2)) + '\nStatus: ' + data[0]['status'])
        text = template.get_text()

        template = ButtonTemplate(text)
        template.add_web_url('Hummingbird URL', data[0]['url'])

        output['input'] = input
        output['output'] = template.get_message()
        output['success'] = True
    except:
        output['success'] = False
        output['error_msg'] = TextTemplate('I couldn\'t find that anime. Please ask me something else!')
    return output
