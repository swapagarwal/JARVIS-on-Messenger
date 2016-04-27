from templates.text import TextTemplate

def process(input, entities=None):
    help = '''Hi there! I'm Jarvis, your personal assistant.\nTell me things like the following:\n
  - define a superhero\n  - iron man 2 movie plot\n  - tell me a joke\n  - wiki html\n  - anything you want book\n  - random quote\n  - usd to eur rate\n
I'm always learning, so do come back and say hi from time to time!\nHave a nice day.'''
    output = {
        'input': input,
        'output': TextTemplate(help).get_message(),
        'success': True
    }
    return output
