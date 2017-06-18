import requests

from templates.text import TextTemplate
from urlparse import urlparse


def process(input, entities):
    output = {}
    try:
        url = entities['url'][0]['value']
        if urlparse(url).scheme:
            url = urlparse(url).hostname
        else:
            url = urlparse('//' + url).hostname
        if url is None:
            raise Exception("Cannot understand url!")
        r = requests.get('https://isitup.org/' + url + '.json')
        data = r.json()
        status = data['status_code']
        if status == 1:
            text = url + ' is up.'
        elif status == 2:
            text = url + ' seems to be down!'
        elif status == 3:
            text = 'Please enter a valid domain to check availability.'
        else:
            raise Exception("Something unexpected happened!")
        output['input'] = input
        output['output'] = TextTemplate(text).get_message()
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
