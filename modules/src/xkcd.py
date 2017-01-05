import requests
import requests_cache
from random import randint
from templates.generic import *
from templates.text import TextTemplate

def process(input, entities=None):
    output = {}
    try:
        with requests_cache.enabled('xkcd_cache', backend='sqlite', expire_after=3600):
            # Get the latest comic
            r = requests.get('http://xkcd.com/info.0.json')
            data = r.json()

            # Get a random comic between the first and the latest one
            r = requests.get('http://xkcd.com/%d/info.0.json' % randint(1, data['num']))
            data = r.json()

        title = data['title']
        item_url = 'http://xkcd.com/' + str(data['num']) + '/'
        explanation_url = 'http://explainxkcd.com/' + str(data['num']) + '/'
        image_url = data['img'].replace('\\', '')
        subtitle = data['alt']

        buttons = ButtonTemplate()
        buttons.add_web_url('xkcd Link', item_url)
        buttons.add_web_url('Explanation Link', explanation_url)

        template = GenericTemplate()
        template.add_element(title=title, item_url=item_url, image_url=image_url, subtitle=subtitle, buttons=buttons.get_buttons())

        output['input'] = input
        output['output'] = template.get_message()
        output['success'] = True
    except:
        error_message = 'There was some error while retrieving data from xkcd.'
        output['error_msg'] = TextTemplate(error_message).get_message()
        output['success'] = False
    return output
