import requests
from templates.text import TextTemplate
from random import choice
import config

def process(input, entities=None):
    output = {}
    try:
        '''
        r = requests.get('http://tambal.azurewebsites.net/joke/random')
        data = r.json()
        output['input'] = input
        output['output'] = TextTemplate(data['joke']).get_message()
        output['success'] = True        
        '''
        
        with open(config.JOKES_SOURCE_FILE,"r") as file:
            dump = file.read() # read the whole file
            jokes_list = dump.split("\'''")[2].split("\n")
            output['input'] = input
            joke = choice(jokes_list).strip() #randomly choose a joke
            if(len(joke)>2): #because there could be null values in the list
                output['output'] = TextTemplate(joke).get_message()
            else:
                output['output'] = TextTemplate(choice(jokes_list).strip()).get_message() #choose again
            output['success']=True

    except:
        output['success'] = False
    return output
