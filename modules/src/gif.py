import config
import json
import os
import requests
from templates.generic import GenericTemplate
from templates.quick_replies import add_quick_reply
from templates.text import TextTemplate

GIPHY_API_KEY = os.environ.get('GIPHY_API_KEY', config.GIPHY_API_KEY)
GIPHY_LOGO_IMG = os.environ.get('GIPHY_LOGO_IMG', config.GIPHY_LOGO_IMG)

def process(input, entities=None):
    output = {}
    try:
        tag = '' if 'gif' not in entities else entities['gif'][0]['value']
        request_url = 'http://api.giphy.com/v1/gifs/random?tag=%s&api_key=%s' % (tag, GIPHY_API_KEY)
        r = requests.get(request_url)
        data = r.json()
        template = GenericTemplate()
        template.add_element(title='Your gif, Sir.', image_url=data['data']['image_url'])
        template.add_element(title='Found on Giphy', image_url=GIPHY_LOGO_IMG)
        postback = {
            'intent': 'gif',
            'entities': entities
        }
        message = add_quick_reply(template.get_message(), 'Another great gif!', json.dumps(postback))
        output = {
            'input': input,
            'output': message,
            'success': True
        }
    except:
        error_message = 'Strange, there seems to be no gif that matches your query. '
        error_message += 'I didn\'t think that would be possible.'
        error_message += '\nPlease ask me something else, like:'
        error_message += '\n  - cat gifs'
        error_message += '\n  - gif of laughing children'
        error_message += '\n  - a southpark gif'
        output['error_msg'] = TextTemplate(error_message).get_message()
        output['success'] = False

    return output
