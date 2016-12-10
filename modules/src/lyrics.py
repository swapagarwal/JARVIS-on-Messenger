import requests
from templates.text import TextTemplate

def process(input, entities):
	output = {}
	try:
		lyrics = entities['lyrics'][0]['value']
		r = requests.get('http://api.chartlyrics.com/apiv1.asmx/SearchLyricText?lyricText=' + lyrics)
		data = r.json()
		output['input'] = input
		template = TextTemplate('Artist: ' + data['ArrayOfSearchLyricResult']['SearchLyricResult']['Artist'] + '\nSong: ' + data['ArrayOfSearchLyricResult']['SearchLyricResult']['Song'])
		output['output'] = template.get_message()
		output['success'] = True
	except:
		error_message = "I am sorry. I wasn't able to find a song with those lyrics. Please try again."
		output['error_msg'] = TextTemplate(error_message).get_message()
		output['success'] = False 
	return output