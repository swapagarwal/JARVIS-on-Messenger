import os
import requests
import config
from templates.button import ButtonTemplate

from templates.text import TextTemplate, TEXT_CHARACTER_LIMIT

COCKTAIL_API_KEY = os.environ.get('COCKTAIL_API_KEY', config.COCKTAIL_API_KEY)


def process(input, entities):
    output = {}
    try:
        query = entities[0]['value']
        # Search in title
        r = requests.get('https://www.thecocktaildb.com/api/json/v1/' + COCKTAIL_API_KEY + '/search.php', params={
            's': query
        })
        data = r.json()
        cocktail = data['drinks'][0]
        cocktail_name = cocktail['strDrink']
        cocktail_instructions = cocktail['strInstructions']
        cocktail_id = cocktail['idDrink']
        cocktail_url = 'https://www.thecocktaildb.com/drink.php?c=' + cocktail_id
        ingredients = ''
        for ingredient_counter in xrange(1, 16):
            ingredient = 'strIngredient' + str(ingredient_counter)
            measure = 'strMeasure' + str(ingredient_counter)
            ingredients += cocktail['strMeasure' + str(ingredient_counter)] + cocktail[
                'strIngredient' + str(ingredient_counter)] + '\n'
            # When there are no more ingredients, break
            if not cocktail[ingredient] or not cocktail[measure]:
                break

        template = TextTemplate()
        template.set_text(cocktail_name + '\n ' + ingredients)
        template.set_post_text('\n' + cocktail_instructions)
        template.set_limit(TEXT_CHARACTER_LIMIT)

        template = ButtonTemplate(template.get_message())
        template.add_web_url('Full Recipe', cocktail_url)

        output['input'] = input
        output['output'] = template.get_message()
        output['success'] = True
    except:
        error_message = 'I couldn\'t find the cocktail you requested.'
        error_message += '\nPlease search for something else, like:'
        error_message += '\n  - margarita cocktail'
        error_message += '\n  - mai tai cocktail recipe'
        error_message += '\n  - martini cocktail'
        output['error_msg'] = TextTemplate(error_message).get_message()
        output['success'] = False
    return output
