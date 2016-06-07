import requests
import wikipedia
from templates.text import TextTemplate

def process(input, entities=None):
    output = {}
    try:  
        output['input'] = input
        #Extracting name from input 
        '''
            format of query is :  Who is Albert Einstein
        '''
        name = input[7:]
        output['output'] = wikipedia.summary(name, sentences=2)
        output['success'] = True
    except:
        output['output'] = 'Please Enter query in correct format'
        output['success'] = False
    return output
