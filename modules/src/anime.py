import requests
from templates.text import TextTemplate

def process(input, entities):
    output = {}
    try:
        word = entities['word'][0]['value']
        r = requests.get('http://hummingbird.me/api/v1/search/anime', params = {'query' : word})	
        data = r.json()
        output['input'] = input
        output['output'] = TextTemplate('Title: ' + data[0]['title'] + '\n' + 'Url: ' + data[0]['url'] + '\n'+ 'Community Rating: ' + data[0]['community_rating'] + '\n'+ 'Status: ' + data[0]['status'] + '\n' ).get_message()
        output['success'] = True
    except:
	#print data
        output['success'] = False
    return output
