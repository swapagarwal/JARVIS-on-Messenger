from templates.text import TextTemplate

def process(input, entities=None):
    eq = entities['math'][0]['values']
    try:
        resp = "Of course Sir,\n the answer is " + eval(eq)
    except SyntaxError:
        resp = "There seems to be an issue with your equation Sir. It might not be supported yet"
    output = {
        'input': input,
        'output': TextTemplate(resp).get_message(),
        'success': True
    }
    return output
