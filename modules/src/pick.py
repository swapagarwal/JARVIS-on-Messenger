import random
from templates.text import TextTemplate

def process(input, entities):
    try:
        options = entities['pick'][0]['value']
        option_list = options.split()
        if option_list == []: raise ValueError("Empty List")
        output = {
            'input': input,
            'output': TextTemplate(random.choice(option_list)).get_message(),
            'success': True
        }

    except:
        error_message = 'I couldn\'t understand what you were saying.'
        error_message += '\nPlease ask me something else, like:'
        error_message += '\n  - pick chinese japanese indian'
        error_message += '\n  - pick soccer basketball'
        error_message += '\n  - pick a b c'
        output['error_msg'] = TextTemplate(error_message).get_message()
        output['success'] = False

    return output
