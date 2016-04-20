import re
import requests

def match(input):
    return bool(re.match(r'^.*jokes?\W*$', input))

def process(input):
    output = {}
    try:
        r = requests.get('https://api.chucknorris.io/jokes/random')
        data = r.json()
        output['input'] = input
        output['output'] = data['value']
        output['success'] = True
    except:
        output['success'] = False
    return output
