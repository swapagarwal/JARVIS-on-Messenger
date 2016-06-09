
import wikipedia
from templates.button import *

def process(input, entities):
    output = {}
    try:
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
        output['error_msg'] = TextTemplate('I could not find any wiki results to do with ' + query + '. Please try again!').get_message()
        output['success'] = False
    return output