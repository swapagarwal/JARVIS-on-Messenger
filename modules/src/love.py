import random

from templates.text import TextTemplate


def process(input, entities=None):
    greetings = [
        'We finish each other\'s sentences, sir.',
        'I love you like crazy, sir.',
        'You are the man of my dreams, sir.',
        'I love you to moon and back.',
        'Making love with you is all I want to do.',
        'Loving you is more than just a dream come true.',
        'This is my perfect moment with you, sir.',
        'With you, forever will not be too long',
        'I truly love you more than I have ever loved anyone.',
        'Please, try to keep in mind that love takes time.',
        'You are my MR.right.',
        'I\'m all yours, sir.',
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
