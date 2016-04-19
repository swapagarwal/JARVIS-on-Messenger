import re
import requests

def match(input):
	return bool(re.match(r'^.*\s+definition$', input))

def process(input):
	output = {}
	word = re.match(r'^(?P<definition>.*)\s+definition$', input).group('definition')
	try:
		r = requests.get("https://glosbe.com/gapi/translate?from=eng&dest=eng&format=json&phrase=" + word + "&pretty=true")
		data = r.json()
		output['input'] = input
		output['output'] = "Definition: " + data['tuc'][0]['meanings'][1]['text']
		output['success'] = True
	except:
		output['success'] = False
	return output