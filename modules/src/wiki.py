import wikipedia
import string
from templates.text import TextTemplate

def process(input, entities):
    output = {}
    try:
        query = entities['wikipedia_search_query'][0]['value']
        data = wikipedia.page(query)
        template = TextTemplate()
        printable = set(string.printable)
        s = filter(lambda x : x in printable, data.summary)
        template.set_text(s)
        template.set_post_text(data.url)
        output['input'] = input
        output['output'] = template.get_message()["text"]
        output['success'] = True
    except:
        output['success'] = False
    return output