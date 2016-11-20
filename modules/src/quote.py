from requests import post
from templates.text import TextTemplate


def process(input, entities=None):
    output = {}
    try:
        send_data = {
            'method': 'getQuote',
            'format': 'json',
            'lang': "en",
            'key': ""
        }
        res = post('http://api.forismatic.com/api/1.0/', send_data)
        content = res.json()
        output['input'] = input
        output['output'] = TextTemplate("{0} - {1}".format(content["quoteText"], content["quoteAuthor"])).get_message()
        output['success'] = True

    except:
        output['success'] = False
    return output
