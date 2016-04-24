import requests
from templates.text import TextTemplate

def process(input, entities=None):
    output = {}
    try:
        r = requests.get('http://tambal.azurewebsites.net/joke/random')
        data = r.json()
        output['input'] = input
        output['output'] = TextTemplate(data['joke']).get_message()
        output['success'] = True
    except:
        output['success'] = False
    return output
