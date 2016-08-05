import random
from templates.text import TextTemplate

def process(input, entities):
    output = {}
    try:
            output['input'] = input
            if random.randrange(0,2,1):
                    output['output'] = TextTemplate("Sure, it's heads!").get_message()
            else:
                    output['output'] = TextTemplate("Sure, it's tails!").get_message()

            output['success'] = True
    except:
            error_message = 'Couldn\'t flip the coin' 
            output['error_msg'] = TextTemplate(error_message).get_message()
            output['success'] = False
    return output
