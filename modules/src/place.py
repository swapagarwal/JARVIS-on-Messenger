import random

from templates.text import TextTemplate

def process(input, entities=None):
    places = [
        'DisneyLand',
        'EverLand',
        'Universal Studios',
        'Lotte World',
        'Ocean World',
        'Caribbean Bay',
        'Europapark'
     ]
     
     message = ' '
     
     output = {
           'input' : input,
           'output' : TextTemplate(message).get_message(),
           'success' : True
     }
        
     return output  
