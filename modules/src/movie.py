import os
from imdb import IMDb

import requests
import requests_cache

import config
from templates.button import *
from utils.YouTube import YouTubeUtil

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
                'api_key': TMDB_API_KEY,
                'append_to_response': 'videos'
            })
            data = r.json()

        # Fetch movie rating from IMDb
        ia = IMDb()
        imdb_id = data['imdb_id']
        imdb_movie = ia.get_movie(imdb_id[2:])

        template = TextTemplate('Title: ' + data['title'] +
                                '\nYear: ' + data['release_date'][:4] +
                                '\nIMDb Rating: ' + str(imdb_movie['rating']) + ' / 10' +
                                '\nOverview: ' + data['overview'])
        text = template.get_text()
        template = ButtonTemplate(text)
        template.add_web_url('IMDb Link', 'https://www.imdb.com/title/' + data['imdb_id'] + '/')

        videos = data['videos']['results']
        # Append first Trailer URL if one exists
        for video in videos:
            if video['type'] == 'Trailer' and video['site'] == 'YouTube':
                template.add_web_url('YouTube Trailer', YouTubeUtil.get_video_url(video['key']))
                break

        output['input'] = input
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
