import wikipedia

def process(input, entities):
    output = {}
    try:
        query = entities['wikipedia_search_query'][0]['value']
        data = wikipedia.summary(query, sentences=5, auto_suggest=True)
        output['input'] = input
        output['output'] = 'Summary :' + data
        output['success'] = True
    except:
        output['success'] = False
    return output
