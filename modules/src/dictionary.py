import requests
from templates.text import TextTemplate

def process(input, entities):
    output = {}
    try:
        word = entities['word'][0]['value']
        token = os.environ.get('WORDS_API_KEY')
        r = requests.get('https://wordsapiv1.p.mashape.com/words/' + word + '/definitions', headers = {'X-Mashape-Key':token})	
        data = r.json()
        output['input'] = input
        output['output'] = TextTemplate('Definition of ' + word + ':\n' + data['definitions']['definition']).get_message()
        output['success'] = True
    except:
        output['success'] = False
    return output
