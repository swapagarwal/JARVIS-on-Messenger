import requests
import config
import os
from difflib import SequenceMatcher
from templates.text import TextTemplate

ZOMATO_API_KEY = os.environ.get('ZOMATO_API_KEY', config.ZOMATO_API_KEY)

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

class rnfException(Exception):
    pass


def process(input, entities):
    output = {}
    output['input'] = input
    try:
        location = entities['restaurant_location'][0]['value'];
        url = 'https://developers.zomato.com/api/v2.1/locations?query=' + location;
        header = {
            'user-key': ZOMATO_API_KEY,
            'Accept': 'application/json'
        };

        r = requests.get(url, headers=header);
        location_data = r.json();

        if location_data['status'] != 'success':
            raise Exception()
        loc = location_data['location_suggestions'][0]

        url = (
            'https://developers.zomato.com/api/v2.1/search'
            '?entity_id={eid}'
            '&entity_type={etype}'
            '&lat={lat}'
            '&lon={lon}'
            '&sort=rating&order=desc').format(
            eid=loc['entity_id'],
            etype=loc['entity_type'],
            lat=loc['latitude'],
            long=loc['longitude']
        );

        restaurant_name = ""
        if 'restaurant_name' in entities:
            restaurant_name += entities['restaurant_name'][0]['value'];
            url += '&query=' + restaurant_name;

        cuisine = ""
        if 'cuisine' in entities:
            cuisine += entities['cuisine'][0]['value']
            url += '&cuisine=' + cuisine

        r = requests.get(url, headers=header);
        res_list = r.json()['restaurants']

        found_res_list = []
        if restaurant_name != "":
            found = False
            for res in res_list:
                if similar(restaurant_name,res['name']) >= 0.8:
                    found = True
                    found_res_list.insert(res)
            if found == False:
                raise rnfException("Could not find the Restaurant Mentioned.")

            output['output'] = TextTemplate(
                # Todo:: Format Output
                ''
            ).get_message()
        else:
            output['output'] = TextTemplate(
                #Todo:: Format Output
                ''
            ).get_message()
        output['success'] = True

    except rnfException as e:
        output['error_msg'] = e
        output['success'] = False
    except:
        error_message = 'I couldn\'t get the restaurant info you asked for.'
        error_message += '\nPlease ask me something else, like:'
        error_message += '\n  - Find restaurants in Delhi'
        error_message += '\n  - restaurants guwahati'
        error_message += '\n  - How\'s Pizza Hut, Gurgaon'
        output['error_msg'] = TextTemplate(error_message).get_message()
        output['success'] = False
    return output
