import random

from templates.text import TextTemplate

def process(input, entities=None):
    Encouragements = [
        'I love you even if you hate me.',
        'Do you really hate me?',
        'Don't hate me.',
        'Don't complain.',
        'I don't hate you.',
    ]
    if entities is not None:
        if 'sender' in entities and 'first_name' in entities['sender']:
            sender_name = entities['sender']['first_name']
            Encouragements = [Encouragement.replace('sir', sender_name) for Encouragement in Encouragements]
            
    output = {
        'input' : input,
        'output': TexTemplate(random.choice(Encouragements)).get_message(),
        'success': True
    }
    return output
