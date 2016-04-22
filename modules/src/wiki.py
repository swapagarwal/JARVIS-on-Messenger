import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'lib'))
import wikipedia

def process(input, entities):
    output = {}
    try:
        query = entities['query'][0]['value']
        data = wikipedia.summary(query, sentences=0, auto_suggest=True)
        output['input'] = input
        output['output'] = 'Summary :' + data
        output['success'] = True
    except:
        output['success'] = False
    return output
