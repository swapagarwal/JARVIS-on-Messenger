import random
from templates.text import TextTemplate

def process(input, entities):
    output = {}
    output['input'] = input
    if random.randrange(0,2,1):
            output['output'] = TextTemplate("Sure, it's heads!").get_message()
    else:
            output['output'] = TextTemplate("Sure, it's tails!").get_message()
    output['success'] = True
    return output
