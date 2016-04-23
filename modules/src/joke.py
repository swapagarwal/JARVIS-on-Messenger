import re
import requests

def process(input, entities=None):
    output = {}
    try:
        r = requests.get('http://tambal.azurewebsites.net/joke/random')
        data = r.json()
        output['input'] = input
        output['output'] = data['joke']
        output['success'] = True
    except:
        output['success'] = False
    return output
