import re
import requests

def match(input):
    return bool(re.match(r'^.*\s+movie$', input))

def process(input):
    output = {}
    movie = re.match(r'^(?P<movie>.*)\s+movie$', input).group('movie')
    try:
        r = requests.get('http://www.omdbapi.com/?t=' + movie + '&plot=short&r=json')
        data = r.json()
        output['input'] = input
        output['output'] = data['Title'] + '\nPlot: ' + data['Plot'] + '\nIMDb Rating: ' + data['imdbRating']
        output['success'] = True
    except:
        output['success'] = False
    return output
