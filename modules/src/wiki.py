import wikipedia

from templates.generic import *
from templates.text import TextTemplate


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
    except wikipedia.exceptions.DisambiguationError as e:
        template = GenericTemplate()
        template.set_image_aspect_ratio_to_square()
        image_url = 'https://en.wikipedia.org/static/images/project-logos/enwiki-2x.png'
        pageids = set()
        for option in e.options:
            try:
                data = wikipedia.page(option)
                if data.pageid in pageids:
                    continue
                pageids.add(data.pageid)
                buttons = ButtonTemplate()
                buttons.add_web_url('Wikipedia Link', data.url)
                payload = {
                    'intent': 'wiki',
                    'entities': {
                        'wiki': [
                            {
                                'value': option
                            }
                        ]
                    }
                }
                buttons.add_postback('Wikipedia Summary', payload)
                template.add_element(title=data.title, item_url=data.url, image_url=image_url,
                                     buttons=buttons.get_buttons())
            except (wikipedia.exceptions.PageError, wikipedia.exceptions.DisambiguationError):
                pass  # Some suggestions don't map to a page; skipping them..
        output['input'] = input
        output['output'] = template.get_message()
        output['success'] = True
    except:
        error_message = 'I couldn\'t find any wikipedia results matching your query.'
        error_message += '\nPlease ask me something else, like:'
        error_message += '\n  - wikipedia barack'
        error_message += '\n  - html wiki'
        error_message += '\n  - who is sachin tendulkar'
        output['error_msg'] = TextTemplate(error_message).get_message()
        output['success'] = False
    return output
