import requests
import requests_cache

import config
from templates.button import *


def process(input, entities):
    output = {}
    try:
        movie = entities['movie'][0]['value']

        # Make a search request to the API to get the movie's TMDB ID.
        # TMDB required attribution notice: "This product uses the TMDb API but is not
        # endorsed or certified by TMDb."

        with requests_cache.enabled('movie_cache', backend='sqlite', expire_after=86400):
            r = requests.get('http://api.themoviedb.org/3/search/movie', params={
                'api_key': config.TMDB_API_KEY,
                'query': movie,
                'page': '1',
                'include_adult': False
            })
            data = r.json()
            tmdb_id = str(data['results'][0]['id'])

            # Make another request to the API using the movie's TMDB ID
            # to get the movie's IMDB ID.

            request_str = 'https://api.themoviedb.org/3/movie/' + tmdb_id


            r = requests.get('https://api.themoviedb.org/3/movie/' + tmdb_id, params ={
                'api_key': config.TMDB_API_KEY
            })
            data = r.json()

        output['input'] = input

        template = TextTemplate('Title: ' + data['title'] +
                                '\nYear: ' + data['release_date'][0:4] +
                                '\nAverage Rating: ' + str(data['vote_average']) + '/10' +
                                '\nOverview: ' + data['overview'])

        text = template.get_text()
        template = ButtonTemplate(text)
        template.add_web_url('IMDb Link', 'https://www.imdb.com/title/' + data['imdb_id'] +'/')
        output['output'] = template.get_message()
        output['success'] = True
    except Exception, e:
        error_message = 'I couldn\'t find that movie.'
        error_message += '\nPlease ask me something else, like:'
        error_message += '\n  - batman movie'
        error_message += '\n  - iron man 2 movie plot'
        error_message += '\n  - What is the rating of happyness movie?'

        output['error_msg'] = TextTemplate(error_message).get_message()
        output['success'] = False
    return output
