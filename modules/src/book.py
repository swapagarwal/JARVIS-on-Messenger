import re
import requests
import config
import os
from xml.etree import ElementTree

GOODREADS_ACCESS_TOKEN = os.environ.get('GOODREADS_ACCESS_TOKEN', config.GOODREADS_ACCESS_TOKEN)

def process(input, entities=None):
    output = {}
    try:
        book_title = entities['book'][0]['value']
        response = requests.get('https://www.goodreads.com/book/title.xml?key='+GOODREADS_ACCESS_TOKEN+'&title=' + book_title)
        data = ElementTree.fromstring(response.content)

        book_node = data.find('book')
        title = book_node.find('title').text
        description = book_node.find('description').text
        link = book_node.find('link').text
        average_rating = book_node.find('average_rating').text
        
        output_data = (title, description, average_rating, link)
        
        output['input'] = input
        output['output'] = "Title: %s<br/>Description: %s<br/>Average Rating: %s<br/> Book link: %s<br/>" % output_data
        output['success'] = True
    except:
        output['success'] = False
    return output
