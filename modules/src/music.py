import requests
import requests_cache
from templates.generic import *
from templates.text import TextTemplate
from datetime import datetime

def process(input, entities):
    output = {}
    try:
        music = entities['music'][0]['value']
        with requests_cache.enabled('music_cache', backend='sqlite', expire_after=3600):
            r = requests.get('https://api.spotify.com/v1/search?q=' + music + '&type=track')
            data = r.json()
        assert(len(data['tracks']['items']) > 0)
        template = GenericTemplate()
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
            template.add_element(title=title, item_url=item_url, image_url=image_url, subtitle=subtitle, buttons=buttons.get_buttons())
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
