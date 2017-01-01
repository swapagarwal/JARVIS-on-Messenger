import requests
import config
import os
from bs4 import BeautifulSoup
from templates.generic import *
from templates.text import TextTemplate


GENIUS_KEY = os.environ.get('GENIUS_API_KEY', config.GENIUS_API_KEY)

def process(input, entities):
    output = {}
    try:      
        query = entities['lyrics'][0]['value']
        base_url = 'http://api.genius.com'
        headers = {'Authorization': 'Bearer %s' % (GENIUS_KEY)} 
        search_url = base_url + '/search'

        r = requests.get(search_url, data={'q': query}, headers=headers)
        r = r.json()
        song_api_path = r['response']['hits'][0]['result']['api_path'] 

        song_url = base_url + song_api_path
        r = requests.get(song_url, headers=headers)
        r = r.json()
        path = r['response']['song']['path']
        page_url = 'http://genius.com' + path

        lyrics_page = requests.get(page_url)
        soup = BeautifulSoup(lyrics_page.text, 'html.parser')
        lyrics_div = soup.find('div',{'class': 'song_body-lyrics'})
        lyrics = lyrics_div.find('p').getText()

        title = query
        item_url = page_url
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



