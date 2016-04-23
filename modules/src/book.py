import requests
import config
import os
from xml.etree import ElementTree

GOODREADS_ACCESS_TOKEN = os.environ.get('GOODREADS_ACCESS_TOKEN', config.GOODREADS_ACCESS_TOKEN)

def process(input, entities=None):
    output = {}
    try:
        book_title = entities['book'][0]['value']
        response = requests.get('https://www.goodreads.com/book/title.xml?key=' + GOODREADS_ACCESS_TOKEN + '&title=' + book_title)
        data = ElementTree.fromstring(response.content)

        book_node = data.find('book')
        title = book_node.find('title').text
        description = book_node.find('description').text[:150] + '...'
        average_rating = book_node.find('average_rating').text
        link = book_node.find('link').text
        goodreads_attribution = "- Powered by Goodreads"

        output_data = (title, description, average_rating, link, goodreads_attribution)

        output['input'] = input
        output['output'] = "Title: %s\nDescription: %s\nAverage Rating: %s\nBook link: %s\n\n%s" % output_data
        output['success'] = True
    except:
        output['success'] = False
    return output
