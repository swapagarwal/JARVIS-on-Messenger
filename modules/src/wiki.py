
import wikipedia
from templates.button import *

def process(input, entities):
    output = {}
    try:
        if 'who is ' in input:
            name = input[7:]
            print name
            output['input'] = input
            output['output'] = wikipedia.summary(name,sentences=2)
            output['success'] = True
        else:
            query = entities['wiki'][0]['value']
            data = wikipedia.page(query)
            output['input'] = input
            template = TextTemplate('Wikipedia summary of ' + data.title + ':\n' + data.summary)
            text = template.get_text()
            template = ButtonTemplate(text)
            template.add_web_url('Wikipedia Link', data.url)
            output['output'] = template.get_message()
            output['success'] = True
    except:
        error_message = 'I couldn\'t find any wikipedia results matching your query.'
        error_message += '\nPlease ask me something else, like:'
        error_message += '\n  - wikipedia barack'
        error_message += '\n  - html wiki'
        error_message += '\n  - wiki sachin tendulkar'
        output['error_msg'] = TextTemplate(error_message).get_message()
        output['success'] = False
    return output
