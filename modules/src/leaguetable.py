import requests
import config
import os
from templates.text import TextTemplate
from BeautifulSoup import BeautifulSoup

def process(input, entities):
    output = {}
    try:
        country = entities['table_location'][0]['value'].upper()

        if country == "ENGLAND":
            path = "premierleague"
        elif country == "SPAIN":
            path = "laligafootball"
        elif country == "GERMANY":
            path = "bundesligafootball"
        elif country == "ITALY":
            path = "serieafootball"
        elif country == "FRANCE":
            path = "ligue1football"
    


        url = 'https://www.theguardian.com/football/' + path + '/table'
        response = requests.get(url)
        html = response.content

        soup = BeautifulSoup(html)
        table = soup.find('tbody')


        rows = table.findAll('tr')
        data = [[td.text for td in tr.findAll("td")] for tr in rows]

        

        holding = ""

        count = 1;
        for i in data:
            holding+= " Position: " 
            holding+=  str(count) 
            holding+= " Team Name: "
            holding+= data[count-1][1]
            holding+= "/n Games Played:"
            holding+= data[count-1][2]
            holding+= " Points:"
            holding+= data[count-1][9] 
            holding+= "/n "
            holding+= "/n "

            count+=1 
               
            
        holding+= ("Powered by Guardian Football")
            output['input'] = input
            output['output'] = TextTemplate(holding).get_message()
            output['success'] = True
    except:
        error_message = 'I couldn\'t get the league table you asked for.'
        error_message += '\nPlease ask me something else, like:'
        error_message += '\n  - tell me the league table in England'
        error_message += '\n  - Spanish team rankings'
        error_message += '\n  - Show me the Bundesliga Table'
        output['error_msg'] = TextTemplate(error_message).get_message()
        output['success'] = False
    return output
