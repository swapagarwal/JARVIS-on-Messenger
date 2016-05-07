import requests
from templates.text import TextTemplate

def process(input, entities):
    output = {}
    try:
        movie = entities['movie'][0]['value']
        r = requests.get('http://www.omdbapi.com/?t=' + movie + '&plot=full&r=json')
        data = r.json()
        output['input'] = input
        template = TextTemplate()
        template.set_text(data['Title'] + '\nPlot: ' + data['Plot'])
        template.set_post_text('\nIMDb Rating: ' + data['imdbRating'] + '\nIMDb Link: http://www.imdb.com/title/' + data['imdbID'])
        output['output'] = template.get_message()
        output['success'] = True
    except:
        output['success'] = False
    return output
