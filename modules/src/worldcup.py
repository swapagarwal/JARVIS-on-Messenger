import requests
import json
from datetime import datetime

from templates.text import TextTemplate

r = requests.get("https://raw.githubusercontent.com/openfootball/world-cup.json/master/2018/worldcup.json")

tourn_info = r.json()

def next_match(team=None):
    current_date = datetime.now()

    if team == None:
        output = "The next match is on {}. {} against {} at {} local time."
        for i in tourn_info["rounds"]:
            for j in i["matches"]:
                match_date = datetime.strptime(j["date"], "%Y-%m-%d")
                if match_date > current_date:
                    output = output.format(match_date.date(), str(j["team1"]["name"]), str(j["team2"]["name"]), str(j["time"]))
                    return output

    elif team != None:
        output = "The next match for {} is on {} against {} at {} local time."
        for i in tourn_info["rounds"]:
            for j in i["matches"]:
                match_date = datetime.strptime(j["date"], "%Y-%m-%d")
                if match_date  > current_date:      #Match is in the future
                    if team.upper() == str(j["team1"]["name"]).upper():
                        return output.format(j["team1"]["name"], str(j["date"]), str(j["team2"]["name"]), str(j["time"]))
                    elif team.upper() == str(j["team2"]["name"]).upper():
                       return output.format(j["team2"]["name"], str(j["date"]), str(j["team1"]["name"]), str(j["time"]))
        return "No more matches for this team in this tournament as it stands :("

def process(input, entities):
    output = {}
    entities=entities[0]
    try:
        if entities["func"] == "next_match":
            output["input"] = input
            output["output"] = next_match(entities["team"])
            output["success"] = True

    except:
        error_message = "Whoops! Something went wrong\n"
        error_message += "You may have requested a feature which is not yet existent in this bot."
        output["error_msg"] = TextTemplate(error_message).get_message()
        output["success"] = False

    return output
