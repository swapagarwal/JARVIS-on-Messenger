import random
from templates.text import TextTemplate

def process(input, entities=None):
    sender_name = 'sir'
    if entities is not None:
        if 'sender' in entities:
            sender_name = entities['first_name']

    greetings = [
        'Have a good day, ' + sender_name + '.',
        'Wonderful ' + sender_name + ', I think it\'s time for my evening nap...',
        'Bye to you as well, ' + sender_name + '.',
        'It was my pleasure talking to you, ' + sender_name,
        'Oh, please do not go!',
    ]
    output = {
        'input': input,
        'output': TextTemplate(random.choice(greetings)).get_message(),
        'success': True
    }
    return output
