import requests
from templates.text import TextTemplate

def process(input, entities):
    output = {}
    try:
        word = entities['word'][0]['value']
        r = requests.get('https://glosbe.com/gapi/translate?from=eng&dest=eng&format=json&phrase=' + word + '&pretty=true')
        data = r.json()
        output['input'] = input
        output['output'] = TextTemplate('Definition of ' + word + ':\n' + data['tuc'][0]['meanings'][0]['text']).get_message()
        output['success'] = True
    except:
        output['success'] = False
    return output
