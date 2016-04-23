import re
import requests

def process(input, entities):
    output = {}
    try:
        word = entities['word'][0]['value']
        r = requests.get('https://glosbe.com/gapi/translate?from=eng&dest=eng&format=json&phrase=' + word + '&pretty=true')
        data = r.json()
        output['input'] = input
        output['output'] = 'Definition of ' + word + ':\n' + data['tuc'][0]['meanings'][0]['text']
        output['success'] = True
    except:
        output['success'] = False
    return output
