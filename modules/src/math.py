import numexpr as ne
from templates.text import TextTemplate


def process(input, entities=None):
    eq = entities['math'][0]['values']
    resp = ""
    try:
        resp = "Of course Sir,\n the answer is " + ne.evaluate(eq)
    except SyntaxError:
        resp = "There seems to be an issue with your equation Sir. "
    output = {
        'input': input,
        'output': TextTemplate(resp).get_message(),
        'success': True
    }
    return output
