import os
import requests

import config

OMDB_API_KEY = os.environ.get('OMDB_API_KEY', config.OMDB_API_KEY)


def process(input, entities):
    output = {}
    try:
        movie = entities['movie'][0]['value']

        r = requests.get('http://www.omdbapi.com/?t=', params={
            'apikey': OMDB_API_KEY,
            't': movie,
        })

        data = r.json()

        output['input'] = input
        output['output'] = 'Title: ' + data['Title']
        output['output'] += '\nRelease Date: ' + data['Released']
        output['output'] += '\nIMDb Rating: ' + data['imdbRating']
        output['output'] += '\nActor(s): ' + data['Actors']
        output['output'] += '\nGenre(s): ' + data['Genre']
        output['output'] += '\nPlot: ' + data['Plot']
        output['success'] = True
    except:
        error_message = 'I couldn\'t find that movie.'
        error_message += '\nPlease ask me something else, like:'
        error_message += '\n  - batman movie'
        error_message += '\n  - iron man 2 movie plot'
        error_message += '\n  - What is the rating of happyness movie?'
        output['success'] = False
    return output
