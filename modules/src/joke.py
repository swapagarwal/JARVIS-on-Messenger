import re
import requests
import random

def process(input, entities=None):
    output = {}
    joke_api_list = ['http://tambal.azurewebsites.net/joke/random',
                     'https://api.chucknorris.io/jokes/random']
    joke_key_list = ['joke', 'value']
    api_count = len(joke_api_list)

    try:
        index = random.randint(0, api_count - 1)
        r = requests.get(joke_api_list[index])
        data_key = joke_key_list[index]
        data = r.json()
        output['input'] = input
        output['output'] = data[data_key]
        output['success'] = True
    except:
        output['success'] = False
    return output
