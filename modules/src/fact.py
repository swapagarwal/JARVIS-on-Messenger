import requests
from templates.text import TextTemplate
from random import choice
import json
import config

def process(input, entities=None):
    output = {}
    try:
        '''
        r = requests.get('http://numbersapi.com/random/trivia', headers={
            'Content-Type': 'application/json'
        })
        data = r.json()
        output['input'] = input
        output['output'] = TextTemplate(data['text']).get_message()
        output['success'] = True
        '''
        with open(config.FACTS_SOURCE_FILE) as facts_file:
            facts = json.load(facts_file)
            facts_list = facts['facts']
            message = TextTemplate(choice(facts_list)).get_message()
			
            postback_fact = {
			    'intent': 'fact',
				'entities': None
				}
			
			
            output['input'] = input
            message = add_quick_reply(message, 'One more!', json.dumps(postback_fact))
            output['output'] = message
            output['success'] = True
    except:
        output['success'] = False
    return output
