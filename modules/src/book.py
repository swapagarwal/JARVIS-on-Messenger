import os
from xml.etree import ElementTree

import requests
import requests_cache
from html2text import html2text

import config
from templates.button import *

GOODREADS_ACCESS_TOKEN = os.environ.get('GOODREADS_ACCESS_TOKEN', config.GOODREADS_ACCESS_TOKEN)


def process(input, entities):
    output = {}
    try:
        book_title = entities['book'][0]['value']

        with requests_cache.enabled('book_cache', backend='sqlite', expire_after=86400):
            response = requests.get(
                'https://www.goodreads.com/book/title.xml?key=' + GOODREADS_ACCESS_TOKEN + '&title=' + book_title)
            data = ElementTree.fromstring(response.content)

        book_node = data.find('book')
        author = book_node.find('authors').find('author').find('name').text
        title = book_node.find('title').text
        description = html2text(book_node.find('description').text)
        average_rating = book_node.find('average_rating').text
        link = book_node.find('link').text
        goodreads_attribution = '- Powered by Goodreads'

        template = TextTemplate()
        template.set_text('Title: ' + title + '\nAuthor: ' + author + '\nDescription: ' + description)
        template.set_post_text('\nAverage Rating: ' + average_rating + ' / 5' + '\n' + goodreads_attribution)

        text = template.get_text()
        template = ButtonTemplate(text)
        template.add_web_url('Goodreads Link', link)

        output['input'] = input
        output['output'] = template.get_message()
        output['success'] = True
    except:
        error_message = 'I couldn\'t find any book matching your query.'
        error_message += '\nPlease ask me something else, like:'
        error_message += '\n  - book timeline'
        error_message += '\n  - harry potter book plot'
        error_message += '\n  - little women book rating'
        output['error_msg'] = TextTemplate(error_message).get_message()
        output['success'] = False
    return output
