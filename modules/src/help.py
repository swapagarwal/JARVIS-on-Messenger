from templates.text import TextTemplate


def process(input, entities=None):
    help = 'Hi there! I\'m Jarvis, your personal assistant.'
    if entities is not None:
        if 'sender' in entities and 'first_name' in entities['sender']:
            sender_name = entities['sender']['first_name']
            help = help.replace('there', sender_name)
    help += '\n\nYou can tell me things like:'
    help += '\n  - define comfort'
    help += '\n  - iron man 2 movie plot'
    help += '\n  - tell me a joke/quote/fact'
    help += '\n  - wiki html'
    help += '\n  - anything you want book'
    help += '\n  - usd to eur rate'
    help += '\n  - death note anime'
    help += '\n  - time in seattle'
    help += '\n  - songs by linkin park'
    help += '\n  - shorten google.com'
    help += '\n  - weather in london'
    help += '\n  - videos of sia'
    help += '\n  - flip a coin'
    help += '\n  - roll a die'
    help += '\n  - show a random xkcd comic'
    help += '\n  - latest news'
    help += '\n  - paradise lyrics'
    help += '\n  - how to perform aerial yoga'
    help += '\n\nI\'m always learning, so do come back and say hi from time to time!'
    help += '\nHave a nice day. :)'

    output = {
        'input': input,
        'output': TextTemplate(help).get_message(),
        'success': True
    }
    return output
