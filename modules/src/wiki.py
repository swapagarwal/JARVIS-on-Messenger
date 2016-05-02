import wikipedia
from templates.text import TextTemplate

def process(input, entities):
    output = {}
    try:
        query = entities['wikipedia_search_query'][0]['value']
<<<<<<< HEAD
        page = wikipedia.page(query)
        data = wikipedia.summary(query, sentences=1)
        output['input'] = input
        output['output'] = 'Wikipedia summary: ' + data + "\n URL: " + page.url
=======
        data = wikipedia.summary(query)
        output['input'] = input
        output['output'] = TextTemplate('Wikipedia Summary: ' + data).get_message()
>>>>>>> swapagarwal/master
        output['success'] = True
    except:
        output['success'] = False
    return output
