import json
import os
from datetime import datetime

import requests
import requests_cache

import config
from templates.generic import *
from templates.text import TextTemplate

SPOTIFY_API_KEY = os.environ.get('SPOTIFY_API_KEY', config.SPOTIFY_API_KEY)
UNAUTHORIZED = 401  # Spotify returns 401 if request fails due to no / invalid auth token


def api_search(auth_token, search_term):
    with requests_cache.enabled('music_cache', backend='sqlite', expire_after=3600):
        headers = {'Authorization': 'Bearer ' + auth_token}
        r = requests.get('https://api.spotify.com/v1/search?q=' + search_term + '&type=track', headers=headers)
    return r


def process(input, entities):
    output = {}
    try:
        music = entities['music'][0]['value']

        with open(config.SPOTIFY_TOKEN_FILE) as token_file:
            token = json.load(token_file)['ACCESS_TOKEN']
        r = api_search(token, music)
        if r.status_code == UNAUTHORIZED:
            auth_url = 'https://accounts.spotify.com/api/token'
            headers = {'Authorization': 'Basic ' + SPOTIFY_API_KEY}
            payload = {'grant_type': 'client_credentials'}
            r = requests.post(auth_url, headers=headers, data=payload)
            new_token = r.json()['access_token']
            with open(config.SPOTIFY_TOKEN_FILE, 'w') as token_file:
                token_dict = {'ACCESS_TOKEN': new_token}
                json.dump(token_dict, token_file)
            r = api_search(new_token, music)
        data = r.json()

        assert (len(data['tracks']['items']) > 0)
        template = GenericTemplate()
        template.set_image_aspect_ratio_to_square()
        for track in data['tracks']['items']:
            title = track['name']
            item_url = track['external_urls']['spotify']
            image_url = track['album']['images'][0]['url']
            artists = []
            for artist in track['artists']:
                artists.append(artist['name'])
            duration = datetime.utcfromtimestamp(track['duration_ms'] / 1000).strftime('%M:%S')
            subtitle = 'By ' + ', '.join(artists) + ' | ' + track['album']['name'] + ' | ' + duration
            buttons = ButtonTemplate()
            buttons.add_web_url('Preview Track', track['preview_url'])
            buttons.add_web_url('Open in Spotify', 'https://embed.spotify.com/openspotify/?spuri=' + track['uri'])
            template.add_element(title=title, item_url=item_url, image_url=image_url, subtitle=subtitle,
                                 buttons=buttons.get_buttons())
        output['input'] = input
        output['output'] = template.get_message()
        output['success'] = True
    except:
        error_message = 'I couldn\'t find any music matching your query.'
        error_message += '\nPlease ask me something else, like:'
        error_message += '\n  - hymn for the weekend song'
        error_message += '\n  - linkin park songs'
        error_message += '\n  - play hotel california'
        output['error_msg'] = TextTemplate(error_message).get_message()
        output['success'] = False
    return output
