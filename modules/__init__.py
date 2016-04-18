import sys
from src import *

def search(input):
    for module in src.__all__:
        if sys.modules['modules.src.' + module].match(input):
            data = sys.modules['modules.src.' + module].process(input)
            if data['success']:
                return data['output']
    return 'I\'m still learning. Check back later!'
