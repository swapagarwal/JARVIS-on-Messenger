import wikipedia
from templates.text import TextTemplate

def process(input, entities):
    output = {}
    try:
        query = entities['wikipedia_search_query'][0]['value']
        data = wikipedia.summary(query)
        output['input'] = input
        output['output'] = TextTemplate('Wikipedia Summary: ' + data).get_message()
        output['success'] = True
    except:
        output['success'] = False
    return output
