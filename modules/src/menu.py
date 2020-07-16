import random

from templates.text import TextTemplate


def process(input, entities=None):
    menus = [
        'cheese pizza',
        'margheta pizza',
        'hamburger', 
        'oil pasta', 
        'beef steak', 
        'rice noodles', 
        'sushi', 
        'sandwich', 
        'chicken salad', 
        'rye bread', 
        'tomato pasta', 
        'curry', 
        'eggs toast', 
        'gorgonzola pizza',
        'BBQ chicken',
        'salmon salad',
        'serial',
        'tandoori chicken',
        'fish dish',
        'dumpling',
        'roast meat',
        'fried rice',
    ]
    c_menu = random.choice(menus)

    message = ''

    if c_menu=='chicken salad' or c_menu=='rye bread' or c_menu=='eggs toast' or c_menu=='sandwich':
        message = 'Simply ' +  c_menu + '.'
    elif c_menu=='oil pasta' or c_menu=='beef steak' or c_menu=='gorgonzola pizza' or c_menu=='margheta pizza':
        message = 'If you\'re with a girlfriend now, I recommend ' + c_menu + '.'
    elif c_menu=='salmon salad' or c_menu=='serial' or c_menu=='fish dish':
        message = 'If you\'re on a diet, I recommend ' + c_menu + '.'
    elif c_menu=='dumpling':
        message = 'How about Chinese food like ' + c_menu +'?'
    else:
        message = 'How about '+ c_menu +'?'
    
    output = {
        'input': input,
        'output': TextTemplate(message).get_message(),
        'success': True
    }
    return output
