import os
import requests
from termcolor import colored as cl
import config
from templates.generic import *
from templates.text import TextTemplate

#api_key = '62ac729f4e89e1.15279050 '
FINANCIAL_API_KEY = os.environ.get('FINANCIAL_API_KEY', config.FINANCIAL_API_KEY)

def process(input, entities=None):
    output = {}
    stock=''
    try:
        url = f'https://eodhistoricaldata.com/api/news?api_token={FINANCIAL_API_KEY}&s={stock}'
        news_json = requests.get(url)
        data= news_json.json()   
        template = GenericTemplate()
        for i in range(5):
            title = data[-i]['title']
            output.append(title)
            buttons = ButtonTemplate()
            buttons.add_web_url('Read more...', url)
            buttons.add_web_url('Powered by Financial News API', 'https://eodhistoricaldata.com/')
            template.add_element(title=title, buttons=buttons.get_buttons())
            print(cl('{}. '.format(i+1), attrs = ['bold']), '{}'.format(title))
        output['input'] = input
        output['output'] = template.get_message()
        output['success'] = True
    except:
        error_message = 'There was some error while retrieving data from Financial News API.'
        output['error_msg'] = TextTemplate(error_message).get_message()
        output['success'] = False     
    return output

