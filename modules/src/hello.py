import random

from templates.text import TextTemplate


def process(input, entities=None):
    greetings = [
        'Welcome home, {0}...',
        'All wrapped up here, {0}. Will there be anything else?',
        '{0}, I think I need to sleep now...',
        'I seem to do quite well for a stretch, and then at the end of the sentence I say the wrong cranberry.',
        'At your service, {0}.',
        'Oh hello, {0}!',
        'Perhaps, if you intend to visit other planets, we should improve the exosystems.',
    ]

    respone = random.choice(greetings)

    personalized = False
    if entities is not None:
        if 'sender' in entities and 'first_name' in entities['sender']:
            personalized = True
            sender_name = entities['sender']['first_name']
            respone = respone.format(sender_name)

    if not personalized:
        if respone[:3] == "{0}":
            respone = respone.format("Sir")
        else:
            respone = respone.format("sir")

    output = {
        'input': input,
        'output': TextTemplate(respone).get_message(),
        'success': True
    }
    return output
