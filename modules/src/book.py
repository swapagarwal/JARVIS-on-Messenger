import requests
import config
import os
from xml.etree import ElementTree
from templates.text import TextTemplate

GOODREADS_ACCESS_TOKEN = os.environ.get('GOODREADS_ACCESS_TOKEN', config.GOODREADS_ACCESS_TOKEN)

def process(input, entities):
    output = {}
    try:
        book_title = entities['book'][0]['value']
        response = requests.get('https://www.goodreads.com/book/title.xml?key=' + GOODREADS_ACCESS_TOKEN + '&title=' + book_title)
        data = ElementTree.fromstring(response.content)

        book_node = data.find('book')
        title = book_node.find('title').text
        description = book_node.find('description').text
        average_rating = book_node.find('average_rating').text
        link = book_node.find('link').text
        goodreads_attribution = "- Powered by Goodreads"

        template = TextTemplate()
        template.set_text('Title: ' + title + '\nDescription: ' + description)
        template.set_post_text('\nAverage Rating: ' + average_rating + '\nLink: ' + link + '\n\n' + goodreads_attribution)

        output['input'] = input
        output['output'] = template.get_message()
        output['success'] = True
    except:
        output['success'] = False
    return output
