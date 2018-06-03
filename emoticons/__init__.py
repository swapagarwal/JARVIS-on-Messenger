import json                
from random import choice
import config
import modules
from templates.quick_replies import add_quick_reply
from templates.text import TextTemplate
# List of all emoticons
__all__ = [ 
  '\U0001f604',
  '\U0001f600',
  '\U0001f601',
  '\U0001f602',
  '\U0001f603'
  ]
  def process(input): 
   output = {} 
   try:
      with open(config.EMOTICONS_SOURCE_FILE) as emoticons_file:
      emoticons = json.load(emoticons_file) 
      emoticons_list = emoticons[input]
      message = TextTemplate(choice(emoticons_list)).get_message()
      output['input'] = input
      output['output'] = message 
      output['success'] = True
      
    except:
      output['success'] = False
    return output
