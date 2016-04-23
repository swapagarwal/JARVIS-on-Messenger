def process(input, entities=None):
    help = '''\n
Hi there. I'm Jarvis, your personal assistant.\nHow may I help you today? Tell me things like the following:\n
  - define a superhero\n  - iron man 2 movie plot\n  - tell me a joke\n  - wiki html\n
I'm always learning, so do come back and say hi from time to time!\nHave a nice day.\n
    '''
    output = {
        'input': input,
        'output': help,
        'success': True
    }
    return output
