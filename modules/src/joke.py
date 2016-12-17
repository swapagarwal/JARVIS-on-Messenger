import requests
from templates.text import TextTemplate
from templates.quick_replies import add_quick_reply
from random import choice
import json
import config

def process(input, entities=None):
    output = {}
    try:
        with open(config.JOKES_SOURCE_FILE) as jokes_file:
            jokes = json.load(jokes_file)
            jokes_list = jokes['jokes']
            joke = TextTemplate(choice(jokes_list)).get_message()
    	    postback_joke = {
    		'intent': 'joke',
    		'entities': None
    		}
    	    postback_quote = {
    		'intent': 'quote',
    		'entities': None
    		}
    	    message = add_quick_reply(joke, 'One more!', json.dumps(postback_joke))
            message = add_quick_reply(message, 'Show me a quote.', json.dumps(postback_quote))
            output['input'] = input
            output['output'] = message
            output['success'] = True
    except:
        output['success'] = False
    return output
