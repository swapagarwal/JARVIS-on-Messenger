import os

import requests
import requests_cache

import config
from templates.button import *
from error_msg import QUERY_ERROR, EXAMPLE_MOVIES

# This product uses the TMDb API but is not endorsed or certified by TMDb.
TMDB_API_KEY = os.environ.get('TMDB_API_KEY', config.TMDB_API_KEY)


def process(input, entities):
    output = {}
    try:
        movie = entities['movie'][0]['value']

        with requests_cache.enabled('movie_cache', backend='sqlite', expire_after=86400):
            # Make a search request to the API to get the movie's TMDb ID
            r = requests.get('http://api.themoviedb.org/3/search/movie', params={
                'api_key': TMDB_API_KEY,
                'query': movie,
                'include_adult': False
            })
            data = r.json()

            assert (len(data['results']) > 0)
            tmdb_id = str(data['results'][0]['id'])

            # Make another request to the API using the movie's TMDb ID to get the movie's IMDb ID
            r = requests.get('https://api.themoviedb.org/3/movie/' + tmdb_id, params={
                'api_key': TMDB_API_KEY
            })
            data = r.json()

        template = TextTemplate('Title: ' + data['title'] +
                                '\nYear: ' + data['release_date'][:4] +
                                '\nAverage Rating: ' + str(data['vote_average']) + ' / 10' +
                                '\nOverview: ' + data['overview'])
        text = template.get_text()
        template = ButtonTemplate(text)
        template.add_web_url('IMDb Link', 'https://www.imdb.com/title/' + data['imdb_id'] + '/')

        output['input'] = input
        output['output'] = template.get_message()
        output['success'] = True
    except:
        error_message = QUERY_ERROR.format('movie') + EXAMPLE_MOVIES
        output['error_msg'] = TextTemplate(error_message).get_message()
        output['success'] = False
    return output
