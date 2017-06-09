import requests
from  bs4 import BeautifulSoup

from templates.text import TextTemplate

def process(input, entitites):
    output = {}
    try:
        url = entities['url'][0]['value']
        strip_list = ['http://','https://','/']
        for item in strip_list:
            url = url.strip(item)
        page = requests.get('https://isitup.org/'+str(url))
        soup = BeautifulSoup(page.content, 'html.parser')
        txt = soup.find('div', id='container').find('p').text
        if txt[0]=='W':
            txt = 'The web domain you entered seems to be invalid!'
        output['input'] = input
        output['output'] = TextTemplate(txt).get_message()
        output['success'] = True
    except:
        error_message = 'There seems to be some problem'
        error_message = '\nPlease ask me something else, like:'
        error_message = '\n - is google.com up'
        error_message = '\n - google.com status'
        output['error_msg'] = TextTemplate(error_message).get_message()
        output['success'] = False
    return output

