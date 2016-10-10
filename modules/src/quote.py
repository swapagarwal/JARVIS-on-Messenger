from requests import get
from templates.text import TextTemplate
from re import sub
from HTMLParser import HTMLParser


def process(input, entities=None):
    output = {}
    try:
        h = HTMLParser()
        res = get('http://quotesondesign.com/wp-json/posts?filter[orderby]=rand&filter[posts_per_page]=1')
        remove_html_tags_pattern = r'(<\w>|</\w>)'
        data = res.json()[0]

        # Remove html paragraph tags. h.unescape() not remove them
        content = sub(remove_html_tags_pattern, "", data["content"])

        # Remove some HTML tags from the response
        escaped_html_content = h.unescape(content)
        author = data['title']
        output['input'] = input
        output['output'] = TextTemplate("{0} - {1}".format(escaped_html_content, author)).get_message()
        output['success'] = True

    except:
        output['success'] = False
    return output
