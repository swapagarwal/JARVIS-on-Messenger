import random

from templates.text import TextTemplate


def process(input, entities=None):
    greetings = [
        'Welcome home, sir...',
        'All wrapped up here, sir. Will there be anything else?',
        'Sir, I think I need to sleep now...',
        'I seem to do quite well for a stretch, and then at the end of the sentence I say the wrong cranberry.',
        'At your service, sir.',
        'Oh hello, sir!',
        'Perhaps, if you intend to visit other planets, we should improve the exosystems.',
    ]

    respone = random.choice(greetings)

    personalized = False
    if entities is not None:
        if 'sender' in entities and 'first_name' in entities['sender']:
            personalized = True
            sender_name = entities['sender']['first_name']
            respone = response.replace('Sir', sender_name)
            respone = response.replace('sir', sender_name)

    output = {
        'input': input,
        'output': TextTemplate(respone).get_message(),
        'success': True
    }
    return output
