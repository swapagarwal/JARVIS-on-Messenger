import requests
from templates.text import TextTemplate
from random import choice
import json
import config

def process(input, entities=None):
    output = {}
    try:
        '''
        r = requests.get('http://tambal.azurewebsites.net/joke/random')
        data = r.json()
        output['input'] = input
        output['output'] = TextTemplate(data['joke']).get_message()
        output['success'] = True        
        '''
        
        with open(config.JOKES_SOURCE_FILE,"r") as file:
            dump = json.load(file) # read the whole file
            jokes_list = dump.get("jokes")
            output['input'] = input
            joke = choice(jokes_list).strip() #randomly choose a joke
            output['output'] = TextTemplate(joke).get_message()
            output['success']=True
    except:
        output['success'] = False
    return output
