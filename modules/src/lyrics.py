import requests
import config
import os
from bs4 import BeautifulSoup
from templates.generic import *
from templates.text import TextTemplate

MUSIX_KEY = os.environ.get('MUSIX_API_KEY', config.MUSIX_API_KEY)

def process(input, entities):
    output = {}
    try:      
        query = entities['lyrics'][0]['value']

        payload = {
            'apikey': MUSIX_KEY,
            'q_track': query,
        }
        
        r = requests.get('http://api.musixmatch.com/ws/1.1/track.search',params=payload)
        data = r.json()

        lyrics_url = data['message']['body']['track_list'][0]['track']['track_share_url']
        track_id = data['message']['body']['track_list'][0]['track']['track_id']

        payload = {
            'apikey': MUSIX_KEY,
            'track_id': track_id,
        }

        r = requests.get('http://api.musixmatch.com/ws/1.1/track.lyrics.get',params=payload)
        data = r.json()
        lyrics = '\n'.join(data['message']['body']['lyrics']['lyrics_body'].split('\n')[:-1])

        title = query
        item_url = lyrics_url
        subtitle = lyrics

        template = GenericTemplate()
        template.add_element(title=title, item_url=item_url, subtitle=subtitle, buttons=[])

        output['input'] = input
        output['output'] = template.get_message()
        output['success'] = True

    except:
        error_message = 'There was some error while retrieving data from genius.com'
        error_message += '\n Please ask me somrthing else, like:'
        error_message += '\n Lyrics for the song Wish you were here'
        output['error_msg'] = TextTemplate(error_message).get_message()
        output['success'] = False      
    return output



