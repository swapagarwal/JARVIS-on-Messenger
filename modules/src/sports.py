import requests
import requests_cache

from templates.button import *

url = 'https://raw.githubusercontent.com/lsv/fifa-worldcup-2018/master/data.json'


def process(input, entities):
    output = {}
    try:
        team = entities['team'][0]['value']
        with requests_cache.enabled('world_cup_cache', backend='sqlite', expire_after=86400):
            r = requests.get(url)
            data = r.json()

        teamID_to_team = {
            1: 'Russia',
            2: 'Saudi Arabia',
            3: 'Egypt',
            4: 'Uruguay',
            5: 'Portugal',
            6: 'Spain',
            7: 'Morocco',
            8: 'Iran',
            9: 'France',
            10: 'Australia',
            11: 'Peru',
            12: 'Denmark',
            13: 'Argentina',
            14: 'Iceland',
            15: 'Croatia',
            16: 'Nigeria',
            17: 'Brazil',
            18: 'Switzerland',
            19: 'Costa Rica',
            20: 'Serbia',
            21: 'Germany',
            22: 'Mexico',
            23: 'Sweden',
            24: 'South Korea',
            25: 'Belgium',
            26: 'Panama',
            27: 'Tunisia',
            28: 'England',
            29: 'Poland',
            30: 'Senegal',
            31: 'Colombia',
            32: 'Japan'
        }

        team_data = data['teams'][teamID(team) - 1]
        abcdefgh = 'abcdefgh'
        group = data['groups'][abcdefgh[(teamID(team) - 1) / 4]]
        group_results = group_matches(teamID(team))
        h_or_a = home_or_away(teamID(team))
        h_or_a_score = home_or_away_score(teamID(team))
        flip_h_or_a_score = flip_home_or_away_score(teamID(team))
        matches = group['matches']

        template = TextTemplate()
        template.set_text('Team: ' + team_data['name'] + '\nGroup: ' + group['name']
            + '\n\nResults:\nGroup Stage:\n\t'

            + team_data['name'] + ' vs. ' + teamID_to_team[matches[group_results[0]][h_or_a[0]]]
            + ': ' + str(matches[group_results[0]][flip_h_or_a_score[0]]) + " | "
            + str(matches[group_results[0]][h_or_a_score[0]]) + '\n\t'

            + team_data['name'] + ' vs. ' + teamID_to_team[matches[group_results[1]][h_or_a[1]]]
            + ': ' + str(matches[group_results[1]][flip_h_or_a_score[1]]) + " | "
            + str(matches[group_results[1]][h_or_a_score[1]]) + '\n\t'

            + team_data['name'] + ' vs. ' + teamID_to_team[matches[group_results[2]][h_or_a[2]]]
            + ': ' + str(matches[group_results[2]][flip_h_or_a_score[2]]) + " | "
            + str(matches[group_results[2]][h_or_a_score[2]])
        )

        text = template.get_text()

        group_name = group['name']

        template = ButtonTemplate(text)
        template.add_web_url(group_name + ' Results', 
            'https://en.wikipedia.org/wiki/2018_FIFA_World_Cup#Group_' + group_name[6])
        template.add_web_url('Tournament Information', 'https://en.wikipedia.org/wiki/2018_FIFA_World_Cup')

        output['input'] = input
        output['output'] = template.get_message()
        output['success'] = True
    except:
        error_message = 'I couldn\'t find any teams from the 2018 FIFA World Cup matching your query.'
        error_message += '\nPlease ask me something else, like:'
        error_message += '\n  - France 2018 World Cup'
        error_message += '\n  - germany 2018 fifa world cup results'
        error_message += '\n  - How did Mexico do in the 2018 FIFA World Cup?'
        output['error_msg'] = TextTemplate(error_message).get_message()
        output['success'] = False
    return output


def teamID(team):
    team = team.lower()
    if team == 'russia':
        return 1
    if team == 'saudi arabia':
        return 2
    if team == 'egypt':
        return 3
    if team == 'uruguay':
        return 4
    if team == 'portugal':
        return 5
    if team == 'spain':
        return 6
    if team == 'morocco':
        return 7
    if team == 'iran':
        return 8
    if team == 'france':
        return 9
    if team == 'australia':
        return 10
    if team == 'peru':
        return 11
    if team == 'denmark':
        return 12
    if team == 'argentina':
        return 13
    if team == 'iceland':
        return 14
    if team == 'croatia':
        return 15
    if team == 'nigeria':
        return 16
    if team == 'brazil':
        return 17
    if team == 'switzerland':
        return 18
    if team == 'costa rica':
        return 19
    if team == 'serbia':
        return 20
    if team == 'germany':
        return 21
    if team == 'mexico':
        return 22
    if team == 'sweden':
        return 23
    if team == 'south Korea':
        return 24
    if team == 'belgium':
        return 25
    if team == 'panama':
        return 26
    if team == 'tunisia':
        return 27
    if team == 'england':
        return 28
    if team == 'poland':
        return 29
    if team == 'senegal':
        return 30
    if team == 'colombia':
        return 31
    if team == 'japan':
        return 32
    return 0


def group_matches(teamID):
    teamID = teamID % 4
    if teamID == 0:
        return [1, 3, 4]
    if teamID == 1:
        return [0, 2, 4]
    if teamID == 2:
        return [0, 3, 5]
    return [1, 2, 5]


def home_or_away(teamID):
    teamID = teamID % 4
    if teamID == 0:
        return ['home_team', 'away_team', 'away_team']
    if teamID == 1:
        return ['away_team', 'away_team', 'home_team']
    if teamID == 2:
        return ['home_team', 'home_team', 'away_team']
    return ['away_team', 'home_team', 'home_team']


def flip_home_or_away_score(teamID):
    teamID = teamID % 4
    if teamID == 0:
        return ['away_result', 'home_result', 'home_result']
    if teamID == 1:
        return ['home_result', 'home_result', 'away_result']
    if teamID == 2:
        return ['away_result', 'away_result', 'home_result']
    return ['home_result', 'away_result', 'away_result']


def home_or_away_score(teamID):
    teamID = teamID % 4
    if teamID == 0:
        return ['home_result', 'away_result', 'away_result']
    if teamID == 1:
        return ['away_result', 'away_result', 'home_result']
    if teamID == 2:
        return ['home_result', 'home_result', 'away_result']
    return ['away_result', 'home_result', 'home_result']