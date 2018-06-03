import random
from templates.text import TextTemplate

def process(input, entities=None):
    greetings = [
         'Don't be upset.',
         'You get ugly when you get angry.',
         'You look good when you smile, not when you're angry.',
    ]
  output = {
       'input': input,
       'output': TextTemplate(random.choice(greetings)).get_message(),
       'success': True
  }
  return output

