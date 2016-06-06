from templates.text import TextTemplate

def process(input, entities=None):
    help = '''Hi there! I'm Jarvis, your personal assistant.\nTell me things like:\n
  - define comfort\n  - iron man 2 movie plot\n  - tell me a joke/quote/fact\n  - wiki html\n  - anything you want book\n  - usd to eur rate\n  - death note anime\n  - time in seattle\n  - songs by linkin park'''
    output = {
        'input': input,
        'output': TextTemplate(help).get_message(),
        'success': True
    }
    return output
