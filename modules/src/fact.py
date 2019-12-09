import modules
from templates.quick_replies import add_quick_reply
import requests
from templates.text import TextTemplate


def process(input, entities=None):
    output = {}
    try:
        URL = "http://jservice.io/api/random"
        r = requests.get(url=URL)
        data = r.json()[0]

        message = "Here's some trivia for you.\n\nQ:\t" + data['question'] + "\nA:\t" + data['answer']

        message = TextTemplate(message).get_message()

        message = add_quick_reply(message, 'Another one!', modules.generate_postback('fact'))
        message = add_quick_reply(message, 'Tell me a joke.', modules.generate_postback('joke'))
        message = add_quick_reply(message, 'Show me a quote.', modules.generate_postback('quote'))
        output['input'] = input
        output['output'] = message
        output['success'] = True
    except:
        output['success'] = False
    return output