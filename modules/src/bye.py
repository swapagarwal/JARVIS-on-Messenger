import random
from templates.text import TextTemplate

def process(input, entities=None):
    greetings = [
        'Have a good day, sir.',
        'Wonderful, I think it\'s time for my evening nap...',
        'Bye to you as well, sir.',
        'It was my pleasure talking to you.',
        'Oh, please do not go!',
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
