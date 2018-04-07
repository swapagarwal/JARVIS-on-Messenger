import random

from templates.text import TextTemplate


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
    output = {
        'input': input,
        'output': TextTemplate(random.choice(greetings)).get_message(),
        'success': True
    }
    return output
