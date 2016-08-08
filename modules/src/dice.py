import random
￼ from templates.text import TextTemplate
￼ 
￼ def process(input, entities):
￼     output = {}
￼     output['input'] = input
      output['output'] = TextTemplate("Dice roll : {} ", random.randint(1,6)).get_message() 
￼     output['success'] = True
￼     return output
