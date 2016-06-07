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
        output['error_msg'] = TextTemplate('I did not manage to get you a fact, sorry! Please try again.').get_message()
        output['success'] = False
    return output
