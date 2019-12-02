import random

import modules
from templates.text import TextTemplate
from templates.quick_replies import add_quick_reply

def process(input, entities=None):
    greetings = [
        'Welcome home, sir...',
        'All wrapped up here, sir. Will there be anything else?',
        'I seem to do quite well for a stretch, and then at the end of the sentence I say the wrong cranberry.',
        'At your service, sir.',
        'Oh hello, sir!',
        'Perhaps, if you intend to visit other planets, we should improve the exosystems.',
    ]
    if entities is not None:
        if 'sender' in entities and 'first_name' in entities['sender']:
            sender_name = entities['sender']['first_name']
            greetings = [greeting.replace('sir', sender_name) for greeting in greetings]

    message = TextTemplate(random.choice(greetings)).get_message()
    message = add_quick_reply(message, 'What do you do?', modules.generate_postback('help'))
    message = add_quick_reply(message, 'Show me a fact.', modules.generate_postback('fact'))
    message = add_quick_reply(message, 'How do I use you?', modules.generate_postback('help'))
    output = {
        'input': input,
        'output': message,
        'success': True
    }
    return output
