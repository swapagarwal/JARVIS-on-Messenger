import modules
from templates.quick_replies import add_quick_reply
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
    help += '\n  - ping google.com'
    help += '\n\nI\'m always learning, so do come back and say hi from time to time!'
    help += '\nHave a nice day. :)'

    message = TextTemplate(help).get_message()
    message = add_quick_reply(message, 'Tell me a joke', modules.generate_postback('joke'))
    message = add_quick_reply(message, 'Roll a die', modules.generate_postback('dice'))
    message = add_quick_reply(message, 'Latest News', modules.generate_postback('news'))
    message = add_quick_reply(message, 'Random xkcd comic', modules.generate_postback('xkcd'))

    output = {
        'input': input,
        'output': message,
        'success': True
    }
    return output
