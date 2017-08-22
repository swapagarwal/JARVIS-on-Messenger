import os
from random import randint

import requests

import config
from templates.text import TextTemplate
from templates.button import ButtonTemplate

EDAMAM_RECIPE_API_KEY = os.environ.get('EDAMAM_RECIPE_API_KEY', config.EDAMAM_RECIPE_API_KEY)
EDAMAM_RECIPE_APP_ID = os.environ.get('EDAMAM_RECIPE_APP_ID', config.EDAMAM_RECIPE_APP_ID)


def process(input, entities):
    output = {}
    try:
        food = entities['recipe'][0]['value']
        r = requests.get('https://api.edamam.com/search?q=' + food +
            '&app_id=' + EDAMAM_RECIPE_APP_ID + '&app_key=' + EDAMAM_RECIPE_API_KEY)
        recipes = r.json()
        recipe_data = recipes['hits'][randint(0, len(recipes['hits']))]['recipe']

        title = 'Title: ' + recipe_data['label']
        ingredients = ''

        for ing in recipe_data['ingredients']:
            ingredients += '\n' + ing['text']

        template = TextTemplate()
        template.set_text(title + ingredients)
        template.set_post_text('Diet labels: ' + recipe_data['dietLabels'] + '\n' + 'Health labels: ' + recipe_data['healthLabels'])
        text = template.get_text()

        template = ButtonTemplate(text)
        template.add_web_url(recipe_data['source'], recipe_data['url'])

        output['input'] = input
        output['output'] = template.get_message()
        output['success'] = True
    except:
        error_message = 'I couldn\'t find that recipe.'
        error_message += '\nPlease ask me something else, like:'
        error_message += '\n  - chicken recipe'
        error_message += '\n  - recipe of roast potatoes'
        error_message += '\n  - What is a chocolate cake recipe?'
        output['error_msg'] = TextTemplate(error_message).get_message()
        output['success'] = False
    return output
