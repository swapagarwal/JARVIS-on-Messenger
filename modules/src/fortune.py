import json
from random import choice

import config
import modules
from templates.quick_replies import add_quick_reply
from templates.text import TextTemplate

def process(input, entities=None):
    output = {}
    try:
        with open(config.FORTUNES_SOURCE_FILE) as fortune_file:
            fortunes_json = json.load(fortune_file)
            fortune_list = fortunes_json['fortunes']
            lucky_numbers_list = fortunes_json['lucky_numbers']
            template = TextTemplate()
            template.set_text('Fortune: ' + choice(fortune_list) + '\nLucky Numbers: ' + choice(lucky_numbers_list))
            message = template.get_message()
            message = add_quick_reply(message, 'One more!', modules.generate_postback('fortune'))
            message = add_quick_reply(message, 'Show me a quote.', modules.generate_postback('quote'))
            message = add_quick_reply(message, 'Tell me a fact.', modules.generate_postback('fact'))
            output['input'] = input
            output['output'] = message
            output['success'] = True
    except:
        output['success'] = False
    return output
