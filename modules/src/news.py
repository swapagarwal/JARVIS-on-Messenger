import os
import config
import requests
import json
from templates.generic import GenericTemplate

NYT_API_KEY = os.environ.get('NYT_API_KEY', config.NYT_API_KEY)

def process(input, entities):
	output = {}
	try:
		topic = str(entities['news'][0]['value'])
		api_response = requests.get(url='https://api.nytimes.com/svc/search/v2/articlesearch.json', params={'api-key': NYT_API_KEY, 'q': topic})
		news_dict = json.loads(api_response.text)
		news = news_dict['response'].get('docs')
		template = GenericTemplate()
		if news:
			for i in range(0,min(2,len(news))):
				title = news[i].get('headline').get('main')
				item_url = news[i].get('web_url')
				image_url = news[i].get('multimedia')[0].get('url') if len(news.get('multimedia')) >= 1 else None
				subtitle = "Data provided by The New York Times"
				buttons = [ {'title': 'View on Web', 'url':item_url} ]
				template.add_element(title=title, item_url=item_url, image_url=image_url, subtitle=subtitle, buttons=buttons)
		output['input'] = input
		output['output'] = template.get_message()
		output['success'] = True
	except:
		output['success'] = False
	return output