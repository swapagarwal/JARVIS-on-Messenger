import requests
import requests_cache
from templates.button import *

def process(input, entities):
    output = {}
    try:
        movie = entities['movie'][0]['value']
        with requests_cache.enabled('movie_cache', backend='sqlite', expire_after=86400):
            r = requests.get('http://www.omdbapi.com/?t=' + movie + '&plot=full&r=json')
            data = r.json()
        output['input'] = input
        template = TextTemplate('Title: ' + data['Title'] + '\nYear: ' + data['Year'] + '\nIMDb Rating: ' + data['imdbRating'] + ' / 10' + '\nPlot: ' + data['Plot'])
        text = template.get_text()
        template = ButtonTemplate(text)
        template.add_web_url('IMDb Link', 'http://www.imdb.com/title/' + data['imdbID'] + '/')
        output['output'] = template.get_message()
        output['success'] = True
    except:
        error_message = 'I couldn\'t find that movie.'
        error_message += '\nPlease ask me something else, like:'
        error_message += '\n  - batman movie'
        error_message += '\n  - iron man 2 movie plot'
        error_message += '\n  - What is the rating of happyness movie?'
        output['error_msg'] = TextTemplate(error_message).get_message()
        output['success'] = False
    return output
