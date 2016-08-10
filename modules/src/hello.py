import random
from templates.text import TextTemplate

def process(input, entities=None):
    sender_name = 'sir'
    if entities is not None:
        if 'sender' in entities:
            sender_name = entities['first_name']

    greetings = [
        'Welcome home, ' + sender_name + '...',
        'All wrapped up here, ' + sender_name + '. Will there be anything else?',
        sender_name + ', I think I need to sleep now...',
        'I seem to do quite well for a stretch, and then at the end of the sentence I say the wrong cranberry.',
        'At your service, ' + sender_name + '.',
        'Oh hello, ' + sender_name + '!',
        'Perhaps, if you intend to visit other planets, we should improve the exosystems.',
    ]
    output = {
        'input': input,
        'output': TextTemplate(random.choice(greetings)).get_message(),
        'success': True
    }
    return output
