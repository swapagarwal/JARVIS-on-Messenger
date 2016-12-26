from templates.button import *
import random, string
import re

def process(input, entities):
    output = {}
    try:
        txt = entities['password'][0]['value']
        candidates = re.findall(r'\d+', txt)
        if(candidates==[]):
            length = 6 # default
        else:
            length=min(10,int(candidates[0])) # keep length limited
        output['input'] = input
        myrg = random.SystemRandom()
        alphabet = string.ascii_letters + string.digits
        pw = str().join(myrg.choice(alphabet) for _ in range(length))
        
        template = TextTemplate('password: ' + pw )
        output['output'] = template.get_message()
        output['success'] = True
    except:
        error_message = 'Sorry, something went wrong'
        error_message += '\nPlease try something else.'
        output['error_msg'] = TextTemplate(error_message).get_message()
        output['success'] = False
    return output
