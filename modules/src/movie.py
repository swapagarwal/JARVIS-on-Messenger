import re
import requests

def process(input, entities):
    output = {}
    try:
        movie = entities['movie'][0]['value']
        r = requests.get('http://www.omdbapi.com/?t=' + movie + '&plot=short&r=json')
        data = r.json()
        output['input'] = input
        output['output'] = data['Title'] + '\nPlot: ' + data['Plot'] + '\nIMDb Rating: ' + data['imdbRating']
        output['success'] = True
    except:
        output['success'] = False
    return output