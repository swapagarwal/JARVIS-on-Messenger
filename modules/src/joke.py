import re
import requests
from random import randint

def process(input, entities=None):
    output = {}
    try:
        output['input'] = input
        if randint(0,1):
            data = requests.get('https://api.chucknorris.io/jokes/random').json()
            output['output'] = data['value']
        else:
            data = requests.get('http://api.yomomma.info/').json()
            output['output'] = data['joke']
        output['success'] = True
    except:
        output['success'] = False
    return output
