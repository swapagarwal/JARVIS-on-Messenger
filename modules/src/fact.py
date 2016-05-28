import requests
from templates.text import TextTemplate

def process(input, entities=None):
    output = {}
    try:
        r = requests.get('http://numbersapi.com/random/trivia', headers={
            'Content-Type': 'application/json'
        })
        data = r.json()
        output['input'] = input
        output['output'] = TextTemplate(data['text']).get_message()
        output['success'] = True
    except:
        output['success'] = False
    return output
