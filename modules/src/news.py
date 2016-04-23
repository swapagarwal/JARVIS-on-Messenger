import re
import requests

# Also not sure exactly what entities is?
# Used as their are often some ads displayed on the first few headlines.
HEADLINE_NUM = 3

def process(input, entities):
	output = {}
	try :
		country = entities['country'][0]['value']
		country = "Australia"
		r = requests.get("https://www.reddit.com/r/"+ country.capitalize())
		news_data = r.json()
		output['input'] = input
		output['output'] = 'Headline news in ' + country.capitalize()  + '\n' + news_data['data']['children'][HEADLINE_NUM]['data']['title']
		output['success']  = True
	except:
		output['success'] = False
	return output

process(input)
