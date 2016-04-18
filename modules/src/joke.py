import re
import requests

def match(input):
    return bool(re.match(r'^.*jokes?\W*$', input))

def process(input):
    output = {}
    try:
        r = requests.get('http://api.icndb.com/jokes/random')
        data = r.json()
        output['input'] = input
        output['output'] = data['value']['joke']
        output['success'] = True
    except:
        output['success'] = False
    return output
