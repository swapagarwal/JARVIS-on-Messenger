import requests
import config
import os
from templates.generic import *
from templates.text import TextTemplate

HOWTO_API_KEY = os.environ.get('HOWTO_API_KEY', config.HOWTO_API_KEY)

def process(input, entities):
    output = {}
    try:
        how = entities['howto'][0]['value']
        with requests_cache.enabled('howto_cache', backend='sqlite', expire_after=7200):
            r = requests.get('https://www.googleapis.com/customsearch/v1?q=' + how + '&cx=014377755534868195414%3Aokgnf_admfs&key=' + HOWTO_API_KEY)
            data = r.json()
        assert(len(data['items']) > 0)
        template = GenericTemplate()
        for i in data['items']:
            title = i['title']
            description = i['snippet']
            item_url = i['link']
            image_url = i['cse_image']['src']
            buttons = ButtonTemplate()
            buttons.add_web_url('Learn more', item_url)
            template.add_element(title=title, item_url=item_url, image_url=image_url, subtitle=description, buttons=buttons.get_buttons())
        output['input'] = input
        output['output'] = template.get_message()
        output['success'] = True
    except:
        error_message = 'I couldn\'t find how to do that.'
        output['error_msg'] = TextTemplate(error_message).get_message()
        output['success'] = False
    return output
