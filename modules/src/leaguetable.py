# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 17:33:00 2018

@author: Adwait
"""
DANIELFOOTBALL_API_KEY='f3e0bba92ced41718adbe56fff4f78e1'

import requests
from templates.text import TextTemplate

def process(input, entities):
    output = {}
    try:
        country = entities['table_location'][0]['value'].upper()

        if country == "ENGLAND":
            nteams=20
            url = "http://api.football-data.org/v1/competitions/445/leagueTable"
        elif country == "SPAIN":
            nteams=20
            url = "http://api.football-data.org/v1/competitions/455/leagueTable"
        elif country == "GERMANY":
            nteams=18
            url = "http://api.football-data.org/v1/competitions/452/leagueTable"
        elif country == "ITALY":
            nteams=20
            url = "http://api.football-data.org/v1/competitions/456/leagueTable"
        elif country == "FRANCE":
            nteams=20
            url = "http://api.football-data.org/v1/competitions/450/leagueTable"        
       
        r = requests.get(url ,headers= { 'X-Auth-Token': DANIELFOOTBALL_API_KEY,})
        rmini=requests.get(url ,headers= { 'X-Auth-Token': DANIELFOOTBALL_API_KEY,'X-Response-Control': 'minified'})
        data=r.json()
        datamini=rmini.json()
        
        table='Pos Team      Pts P  W  D\n'
        for i in range(nteams):
            table+=(str(data['standing'][i]['position'])+'.  ')[:3]
            table+=(datamini['standing'][i]['team']+'                 ')[:10]
            table+=' '+(str(data['standing'][i]['points'])+'  ')[:3]
            table+=' '+(str(data['standing'][i]['playedGames'])+'  ')[:3]
            table+=(str(data['standing'][i]['wins'])+'  ')[:3]
            table+=str(data['standing'][i]['draws'])
            table+='\n'
            
        table+= ("Powered by https://api.football-data.org/about")        
        output['input'] = input
        output['output'] = TextTemplate(table).get_message()
        output['success'] = True
        
        
    except:
        error_message = 'I couldn\'t get the league table you asked for.'
        error_message += '\nPlease ask me something else, like:'
        error_message += '\n  - tell me the league table in England'
        error_message += '\n  - Spanish football team rankings'
        error_message += '\n  - Show me the Bundesliga Table'
        output['error_msg'] = TextTemplate(error_message).get_message()
        output['success'] = False
    return output

