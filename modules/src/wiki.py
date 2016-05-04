import wikipedia
from templates.text import TextTemplate

def process(input, entities):
    output = {}
    try:
        query = entities['wikipedia_search_query'][0]['value']
        data = wikipedia.page(query)
        template = TextTemplate()
        template.set_text(data.summary)
        template.set_post_text(data.url)
        output['input'] = input
        output['output'] = template.get_message()
        output['success'] = True
    except:
        output['success'] = False
        
    return output