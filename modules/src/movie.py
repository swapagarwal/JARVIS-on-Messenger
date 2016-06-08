import requests
from templates.button import *

def process(input, entities):
    output = {}
    try:
        movie = entities['movie'][0]['value']
        r = requests.get('http://www.omdbapi.com/?t=' + movie + '&plot=full&r=json')
        data = r.json()
        output['input'] = input
        template = TextTemplate('Title: ' + data['Title'] + '\nYear: ' + data['Year'] + '\nIMDb Rating: ' + data['imdbRating'] + '\nPlot: ' + data['Plot'])
        text = template.get_text()
        template = ButtonTemplate(text)
        template.add_web_url('IMDb Link', 'http://www.imdb.com/title/' + data['imdbID'] + '/')
        output['output'] = template.get_message()
        output['success'] = True
    except:
        output['error_msg'] = TextTemplate('I could not find anything to do with ' + movie + ', sorry. Please try again!').get_message()
        output['success'] = False
    return output