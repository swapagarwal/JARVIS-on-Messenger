import requests
import json

from templates.text import TextTemplate

def process(input, entitites):
    output = {}
    try:
        url = entities['url'][0]['value']
        orig_url = url
        strip_list = ['http://','https://','/']
        for item in strip_list:
            url = url.strip(item)
        page = requests.get('https://isitup.org/'+url+'.json')
        page = json.loads(page.text)
        status = page['status_code']
        if status == 1:
            txt = orig_url + ' is up!'
        elif status == 2:
            txt = orig_url + ' seems to be down!'
        else :
            txt = 'I need a valid domain to check!'
        output['input'] = input
        output['output'] = TextTemplate(txt).get_message()
        output['success'] = True
    except:
        error_message = 'There seems to be some problem'
        error_message = '\nPlease ask me something else, like:'
        error_message = '\n - is google.com up'
        error_message = '\n - google.com status'
        error_message = '\n - ping google.com'
        output['error_msg'] = TextTemplate(error_message).get_message()
        output['success'] = False
    return output

