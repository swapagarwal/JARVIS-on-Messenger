import numexpr as ne
from templates.text import TextTemplate

def process(input, entities=None):
    eq = entities['math'][0]['values']
    resp = ""
    try:
        resp = "The result is " + ne.evaluate(eq)
    except SyntaxError:
        resp = "I think there is a problem with the calculation"
        
   output = {
        'input' : input,
        'output': TextTemplate(resp).get_message(),
        'success':True
  }
  return output
