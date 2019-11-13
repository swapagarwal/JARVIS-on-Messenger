import config
import modules
import os
import sys
import tweepy

from templates.button import ButtonTemplate
from templates.quick_replies import add_quick_reply
from templates.text import TextTemplate

HASHTAGS_PER_REQUEST = 10

TWITTER_CONSUMER_KEY = os.environ.get('TWITTER_CONSUMER_KEY', config.TWITTER_CONSUMER_KEY)
TWITTER_CONSUMER_SECRET = os.environ.get('TWITTER_CONSUMER_SECRET', config.TWITTER_CONSUMER_SECRET)
TWITTER_ACCESS_TOKEN = os.environ.get('TWITTER_ACCESS_TOKEN', config.TWITTER_ACCESS_TOKEN)
TWITTER_ACCESS_TOKEN_SECRET = os.environ.get('TWITTER_ACCESS_TOKEN_SECRET', config.TWITTER_ACCESS_TOKEN_SECRET)

def convert_to_shortform(num):
    ''' convert big numbers into human redable small form
        parameters:
           * num (int)

        e.g
        * 1432 -> 1.4K
        * 14857400 -> 14.8M
    '''

    if num == None: return ''
    suffixes = ['', 'K', 'M', 'B', 'T', 'P', 'E', 'Z', 'Y']
    num_str = '{:,}'.format(num)    # 1324674 -> 1,324,674
    comma_count = num_str.count(',')

    if comma_count == 0:
        return num_str
    num_arr = num_str.split(',', 1)

    return '{}.{}{}'.format(num_arr[0], num_arr[1][0:1], suffixes[comma_count])


def process(input, entities):
    output = {}

    try:
        # get cordinates if extracted from input address
        coords = None
        if 'location' in entities and entities['location'][0].get('values') != None:
            coords = entities['location'][0]['values'][0]['coords']

        auth = tweepy.OAuthHandler(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET)
        auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
        api = tweepy.API(auth)

        # set default woeid as 1 (worldwide)
        woeid = 1 # (Where On Earth IDentifier) assigned by yahoo
        title = 'Worldwide Trends'
        place_type = 'global'
        offset = 0

        if 'postback' in entities:
            title = entities['postback']['title']
            woeid = entities['postback']['woeid']
            place_type = entities['postback']['place_type']
            offset = entities['postback'].get('offset', 0)

        elif coords != None:
            closest_places = api.trends_closest(lat=coords['lat'], long=coords['long'])

            closest_place = closest_places[0]
            city = closest_place['name'].strip().title()
            country = closest_place['country'].strip().title()
            city_woeid = closest_place['woeid']
            country_woeid = closest_place['parentid']

            if city == country:
                title = '{} Trends'.format(country)
                woeid = country_woeid
                place_type = 'country'
            else:
                title = '{} Trends'.format(city)
                woeid = city_woeid
                place_type = 'city'

        button_temp = ButtonTemplate(title)

        hashtags = api.trends_place(woeid)

        for id, hashtag in enumerate(hashtags[0]['trends'][offset:offset + HASHTAGS_PER_REQUEST]):
            if hashtag['promoted_content'] != None: continue

            text = u' {} | {} '.format(offset + 1 + id, hashtag['name'])
            if hashtag['tweet_volume'] != None:
                text += u'\n({})'.format(convert_to_shortform(hashtag['tweet_volume']))

            button_temp.add_web_url(text, hashtag['url'])

        # add 'Show more' postback at the end of list
        postback_entities = {
            'postback': {
                'title': title,
                'woeid': woeid,
                'place_type': place_type,
                'offset': offset + HASHTAGS_PER_REQUEST,
            }
        }
        button_temp.add_postback('Show more ...',
            modules.generate_postback('twitter', postback_entities))
        msg = button_temp.get_message()

        # add all relavant quick replies
        if place_type == 'city':
            postback_entities = {
                'postback': {
                    'title': '{} Trends'.format(country),
                    'woeid': country_woeid,
                    'place_type': 'country',
                }
            }
            msg = add_quick_reply(msg, '{} Trends'.format(country),
                    modules.generate_postback('twitter', postback_entities))

        if place_type != 'global':
            postback_entities = {
                'postback': {
                    'title': 'Worldwide Trends',
                    'woeid': 1,
                    'place_type': 'global'
                }
            }
            msg = add_quick_reply(msg, 'Worldwide Trends',
                    modules.generate_postback('twitter', postback_entities))

        output['input'] = input
        output['output'] = msg
        output['success'] = True

    except:
        error_message = 'I couldn\'t get trends based on your query'
        error_message += '\nPlease ask me something else, like:'
        error_message += '\n  - trending hashtags'
        error_message += '\n  - Newyork trends'
        error_message += '\n  - twitter trend worlwide'
        error_message += '\n  - trend in India'
        output['error_msg'] = TextTemplate(error_message).get_message()
        output['success'] = False

    return output
