import os
import json
import requests
import random
import difflib

import config
from templates.generic import *
from templates.text import TextTemplate

ZOMATO_API_KEY = os.environ.get('ZOMATO_API_KEY', config.ZOMATO_API_KEY)

def process(input,entities):
	output = {}
	try:
		requested_location = entities['restaurant_location'][0]['value']

		header = {'user-key': ZOMATO_API_KEY, 'Accept': 'application/json'}
		response = requests.get('https://developers.zomato.com/api/v2.1/locations?query=' + requested_location, headers=header)
		
		if response.ok:
			content = response.json()
			try:
				location = content['location_suggstions'][0]
			except (KeyError,IndexError):
				error_message = 'I couldn\'t find any restaurants matching your query.'
				error_message += '\nPlease ask me something else, like:'
				error_message += '\n  - Is Giordano\'s pizza in Chicago good?'
				error_message += '\n  - Chipotle in Evanston'
				error_message += '\n  - What are some restaurants in Chicago?'
				output['error_msg'] = TextTemplate(error_message).get_message()
				output['success'] = False

				return output

			search_url = 'https://developers.zomato.com/api/v2.1/search?entity_id={eid}&entity_type={etype}&lat={lat}&lon={lon}&sort=rating&order=desc'.format(
			eid=location['entity_id'],
			etype=location['entity_type'],
			lat=location['latitude'],
			lon=location['longitude'])
		
			restaurant_name = ''
			restaurant_cuisine = ''

			if 'restaurant_name' in entities:
				restaurant_name = entities['restaurant_name'][0]['value']
				search_url += '&q={restaurant_name}'.format(restaurant_name=restaurant_name)

			if 'cuisine' in entities:
				restaurant_cuisine = entities['cuisine'][0]['value']
				search_url += '&cuisines={restaurant_cuisine}'.format(restaurant_cuisine=restaurant_cuisine)

			response = requests.get(search_url,headers=header)
			if response.ok:
				content = response.json()['restaurants']

				try:
					if restaurant_name == '':
						rand_restaurant = content[random.randrange(0,len(content))]

						template = TextTemplate('Name: ' + rand_restaurant['name'] +
												'\nAddress: ' + rand_restaurant['address'] +
												'\nCuisine: ' + rand_restaurant['cuisines'] +
												'\nAverage Price for Two: ' + rand_restaurant['average_cost_for_two'])
						text = template.get_text()
						template = ButtonTemplate(text)
						template.add_web_url('Restaurant Link', rand_restaurant['url'])

						output['input'] = input
						output['output'] = template.get_message()
						output['success'] = True
					else:
						restaurant_list = []
						most_relevant = 0
						search_success = False
						for restaurant in content:
							rest_name = restaurant['name']
							relevance = difflib.SequenceMatcher(None,restaurant_name,rest_name).ratio()
							if relevance >= .75:
								search_success = True
								if relevance >= most_relevant:
									restaurant_list.insert(0,restaurant)
									most_relevant = relevance
						if not search_success:
							template = TextTemplate('I couldn\'t find any restaurants matching your query. Please try asking me something else.')
							output['input'] = input
							output['output'] = template.get_message()
							output['success'] = False
						else:
							out_rest = restaurant_list[0]
							template = TextTemplate('Name: ' + out_rest['name'] +
													'\nAddress: ' + out_rest['address'] +
													'\nCuisine: ' + out_rest['cuisines'] +
													'\nAverage Price for Two: ' + out_rest['average_cost_for_two'])
				
							text = template.get_text()
							template = ButtonTemplate(text)
							template.add_web_url('Restaurant Link', out_rest['url'])
				
							output['input'] = input
							output['output'] = template.get_message()
							output['success'] = True
				except (KeyError,IndexError):
					error_message = 'I couldn\'t find any restaurants matching your query.'
					error_message += '\nPlease ask me something else, like:'
					error_message += '\n  - Is Giordano\'s pizza in Chicago good?'
					error_message += '\n  - Chipotle in Evanston'
					error_message += '\n  - What are some restaurants in Chicago?'
					output['error_msg'] = TextTemplate(error_message).get_message()
					output['success'] = False

					return output

	except:
		error_message = 'I couldn\'t find any restaurants matching your query.'
		error_message += '\nPlease ask me something else, like:'
		error_message += '\n  - Is Giordano\'s pizza in Chicago good?'
		error_message += '\n  - Chipotle in Evanston'
		error_message += '\n  - What are some restaurants in Chicago?'
		output['error_msg'] = TextTemplate(error_message).get_message()
		output['success'] = False

	return output
