import requests
from random import randint
from datetime import datetime, timedelta, date
from templates.generic import *
from templates.text import TextTemplate

def process(input, entities=None):
    output = {}
    try:
        r = requests.get('http://xkcd.com/info.0.json')
        data = r.json()
        max_num = data['num']

        r = requests.get('http://xkcd.com/%d/info.0.json' % randint(1, max_num) )
        data = r.json()

        title = data['title']
        item_url = 'http://xkcd.com/' + str(data['num']) + '/'
        image_url = data['img'].replace('\\', '')
        subtitle = data['alt']

        template = GenericTemplate()
        template.add_element(title=title, item_url=item_url, image_url=image_url, subtitle=subtitle, buttons=[])

        output['input'] = input
        output['output'] = template.get_message()
        output['success'] = True
    except:
        error_message = 'There was some error while retrieving data from xkcd.'
        output['error_msg'] = TextTemplate(error_message).get_message()
        output['success'] = False
    return output
