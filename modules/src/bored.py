import random

import modules
from templates.text import TextTemplate
from templates.quick_replies import add_quick_reply

#a tuple of suggestions. should make sense after the phrase "You should..."
suggestions = ("read a book", "watch a movie", "go for a walk", "work out", 
  "check on a friend", "learn the Python programming language", "watch a new movie",)

def process(input, entities=None):
  suggestion = random.choice(suggestions)
  message_text = "You should {}".format(suggestion)
  message = TextTemplate(message_text).get_message()
  message = add_quick_reply(message, "Try another activity", modules.generate_postback("bored"))
  output = {
        'input': input,
        'output': message,
        'success': True
    }
  return output
