from pycricbuzz import Cricbuzz
import requests
import requests_cache
from templates.button import *


def process(input, entities=None):
    output = {}
    try:
        cricket = Cricbuzz()
        matches = cricket.matches()
        text_data=""
        template = TextTemplate()
        for match in matches:
            cric_data=cricket.livescore(match['id'])
            text_data+=cric_data['matchinfo']['mnum']+"\n"+cric_data['matchinfo']['mchdesc']+"\n"
            text_data+=cric_data['batting']['team']+"\t"+cric_data['batting']['score'][0]['runs']+"/"+cric_data['batting']['score'][0]['wickets']+"\n"
            text_data+=cric_data['bowling']['team']+"\t"+cric_data['bowling']['score'][0]['runs']+"/"+cric_data['bowling']['score'][0]['wickets']+"\n"
            text_data+=cric_data['matchinfo']['status']+"\n"+"*"*10+"\n"
        template.set_text(text_data)
        text = template.get_text()
        template = ButtonTemplate(text)
        template.add_web_url('CricBuzz Live', 'http://www.cricbuzz.com/cricket-match/live-scores')

        output['input'] = input
        output['output'] = template.get_message()
        output['success'] = True
    except:
        error_message = 'There was some error while retrieving data from Cricbuzz'
        output['error_msg'] = TextTemplate(error_message).get_message()
        output['success'] = False
    return output
