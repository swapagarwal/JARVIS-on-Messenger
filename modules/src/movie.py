import requests
import requests_cache
from templates.button import *
from error_msg import QUERY_ERROR, EXAMPLE_MOVIES

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
        error_message = QUERY_ERROR.format('movie') + EXAMPLE_MOVIES
        output['error_msg'] = TextTemplate(error_message).get_message()
        output['success'] = False
    return output
