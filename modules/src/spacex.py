import requests
import pprint
import json
from datetime import datetime
from templates.text import TextTemplate

def convert_text(text):
    return text.encode('utf-8')

def process(input, entities=None):
    pp = pprint.PrettyPrinter(indent=4)
    output = {}
    #if the next keyword is detected in the query
    if "next" in entities[0]["value"]:
        try:
            response = requests.get("https://api.spacexdata.com/v3/launches/next")
            data = json.loads(response.content)
            pp.pprint(data)
            results = "The next launch is"
            results += "\nMission: " + convert_text(data['mission_name'])
            results += "\nDescription: " + convert_text(data['details'])

            # get datetime using unix timestamp
            timestamp = int(data['launch_date_unix'])
            date_timestamp = datetime.fromtimestamp(timestamp)
            date_string = date_timestamp.strftime('%b %d %Y %H:%M:%S')
            results += "\nDate and time (Unix): " + date_string

            results += "\nVehicle: " + convert_text(data["rocket"]["rocket_name"])

            template = TextTemplate(results)
            output['input'] = input
            output['output'] = template.get_message()
            output['success'] = True
        except:
            error_message = 'I couldn\'t find any spacex results matching your query.'
            error_message += '\nPlease ask me something else, like:'
            error_message += '\n  - spacex launch'
            output['error_msg'] = TextTemplate(error_message).get_message()
            output['success'] = False
    return output