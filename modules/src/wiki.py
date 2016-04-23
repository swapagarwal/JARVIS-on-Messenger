import wikipedia

def process(input, entities):
    output = {}
    try:
        query = entities['wikipedia_search_query'][0]['value']
        data = wikipedia.summary(query, sentences=1)
        output['input'] = input
        output['output'] = 'Wikipedia summary: ' + data
        output['success'] = True
    except:
        output['success'] = False
    return output
