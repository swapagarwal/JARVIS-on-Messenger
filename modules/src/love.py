import random

from templates.text import TextTemplate


def process(input, entities=None):
    greetings = [
        'Making love with you is all I want to do',
        'We finish each other\'s sentences.',
        'I love you like crazy.',
        'I missed you tons.',
        'This is my perfect moment with you.',
        'I love you to moon and back.',
        'I truly love you more than I have ever loved anyone',
        'Don\'t kiss me,if you kiss me. I won\'t be able to leave.',
    ]
   
    output = {
        'input': input,
        'output': TextTemplate(random.choice(greetings)).get_message(),
        'success': True
    }
    return output
