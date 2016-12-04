import requests
from templates.text import TextTemplate
import json
import config

def process(input, entities=None):
    output = {}
    try:
        r = requests.get('http://xkcd.com/info.0.json')
        data = r.json()
        number = data['num']
        title = data['title']
        link = data['img']

        output['input'] = input
        output['output'] = TextTemplate('Number: ' + number + '\nTitle: ' + title + '\nLink: ' + link).get_message()
        output['success'] = True
    except:
        error_message = 'Error retrieving latest XKCD'
        ouput['error_message'] = TextTemplate(error_message).get_message()
        output['success'] = False
    return output
