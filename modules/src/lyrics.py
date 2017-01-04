import requests
import config
import os
from templates.button import *

MUSIXMATCH_API_KEY = os.environ.get('MUSIXMATCH_API_KEY', config.MUSIXMATCH_API_KEY)

def process(input, entities):
    output = {}
    try:
        query = entities['lyrics'][0]['value']
        r = requests.get('http://api.musixmatch.com/ws/1.1/track.search', params={
            'apikey': MUSIXMATCH_API_KEY,
            'q_track': query,
            's_track_rating': 'desc'
        })
        data = r.json()
        track = data['message']['body']['track_list'][0]['track']
        track_id = track['track_id']
        track_name = track['track_name']
        artist_name = track['artist_name']
        lyrics_url = track['track_share_url']

        r = requests.get('http://api.musixmatch.com/ws/1.1/track.lyrics.get', params={
            'apikey': MUSIXMATCH_API_KEY,
            'track_id': track_id
        })
        data = r.json()
        lyrics = data['message']['body']['lyrics']['lyrics_body']

        template = TextTemplate()
        template.set_text('Here are the lyrics of ' + track_name + ' by ' + artist_name + ':\n' + lyrics)
        template.set_post_text('\n- Powered by MusiXmatch')
        template.set_limit(TEXT_CHARACTER_LIMIT)

        template = ButtonTemplate(template.get_text())
        template.add_web_url('Full Lyrics', lyrics_url)

        output['input'] = input
        output['output'] = template.get_message()
        output['success'] = True
    except:
        error_message = 'I couldn\'t find any lyrics matching your query.'
        error_message += '\nPlease ask me something else, like:'
        error_message += '\n  - paradise lyrics'
        error_message += '\n  - lyrics of the song hall of fame'
        error_message += '\n  - What are the lyrics to see you again?'
        output['error_msg'] = TextTemplate(error_message).get_message()
        output['success'] = False      
    return output
