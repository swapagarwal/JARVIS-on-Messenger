import requests

from templates.generic import *
from templates.text import TextTemplate
from urlparse import urlparse

def process(input, entities):
    output = {}
    try:
        url = entities['url'][0]['value']
        if not urlparse(url).scheme:
            url = "https://" + url
        hostname = urlparse(url).hostname
        if hostname is None:
            raise Exception("Please enter a valid hostname to check availability.")
        r = requests.get('https://isitup.org/' + hostname + '.json')
        data = r.json()
        status = data['status_code']
        if status == 1:
            text = hostname + ' is up.'
            image_url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/71/Arbcom_ru_ready.svg/240px-Arbcom_ru_ready.svg.png'
        elif status == 2:
            text = hostname + ' seems to be down!'
            image_url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/Arbcom_ru_withdrawn.svg/240px-Arbcom_ru_withdrawn.svg.png'
        elif status == 3:
            text = 'Please enter a valid domain to check availability.'
            image_url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e2/Twemoji_2755.svg/240px-Twemoji_2755.svg.png'
        else:
            raise Exception("Something unexpected happened!")
        template = GenericTemplate()
        template.add_element(title=text, image_url=image_url)
        output['input'] = input
        output['output'] = template.get_message()
        output['success'] = True
    except:
        error_message = 'There seems to be a problem looking up that domain.'
        error_message += '\nPlease ask me something else, like:'
        error_message += '\n - is google.com up'
        error_message += '\n - google.com status'
        error_message += '\n - ping google.com'
        output['error_msg'] = TextTemplate(error_message).get_message()
        output['success'] = False
    return output
