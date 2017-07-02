import random,re
from templates.text import TextTemplate

def process(input, entities):
    try:
        pattern='^pick\s'
        choices=entities['choices'][0]['value']
        choices=re.split(pattern,choices)
        choices = choices[1:].split(' ')
        if choices == []: raise ValueError("Empty List")
        output = {
            'input': input,
            'output': TextTemplate(random.choice(choices)).get_message(),
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