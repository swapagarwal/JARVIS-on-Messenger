import json
import requests
import config
import os
from requests.utils import quote
from requests_oauthlib import OAuth1
from templates.generic import *
from templates.text import TextTemplate

TWI_CONSUMER_KEY = os.environ.get('TWI_CONSUMER_KEY', config.TWI_CONSUMER_KEY)
TWI_CONSUMER_SECRET = os.environ.get(
    'TWI_CONSUMER_SECRET', config.TWI_CONSUMER_SECRET)
TWI_ACCESS_TOKEN = os.environ.get('TWI_ACCESS_TOKEN', config.TWI_ACCESS_TOKEN)
TWI_ACCESS_TOKEN_SECRET = os.environ.get(
    'TWI_ACCESS_TOKEN_SECRET', config.TWI_ACCESS_TOKEN_SECRET)

TWI_URL_SEARCH_API = 'https://api.twitter.com/1.1/search/tweets.json?q='
TWI_USER_TIMELINE_API = 'https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name='

params = {'search':
          {'count': 1,
           'result_type': 'mixed',
           'include_entities': 'true',
           'extended_tweet': 'true'
           },
          'timeline':
          {'count': 1,
           'exclude_replies': 'true',
           'extended_tweet': 'true'
           }
          }


def get_oauth():
    """ Generates an OAuth object """

    oauth = OAuth1(TWI_CONSUMER_KEY,
                   client_secret=TWI_CONSUMER_SECRET,
                   resource_owner_key=TWI_ACCESS_TOKEN,
                   resource_owner_secret=TWI_ACCESS_TOKEN_SECRET)
    return oauth


def getUrl(tweet):
    """ getUrl by author or trendy topic """

    if tweet.startswith('@'):
        author = tweet[1:]
        req = requests.get(url=TWI_USER_TIMELINE_API + author, headers={
                           'content-type': 'application/json'}, params=params['timeline'], auth=get_oauth())
        latest = req.json()[0]
        tweet_id = latest['id_str']
        url = 'https://twitter.com/%s/status/%s' % (author, tweet_id)
    else:
        req = requests.get(url=TWI_URL_SEARCH_API + tweet, headers={
                           'content-type': 'application/json'}, params=params['search'], auth=get_oauth())
        trendy = req.json()['statuses'][0]
        author = trendy['user']['screen_name']
        tweet_id = req['id']
        url = 'https://twitter.com/%s/status/%s' % (author, tweet_id)

    return url, req


def getTitle(req, tweet):
    """ Build title with hashtags """

    try:
        hashtags = req['entities']['hashtags']
        if not hastags:
            raise KeyError
        title = ''
        for tag in hashtags:
            title += '#%s ' % tag['text']
        title = title.strip()
    except KeyError:
        if tweet[0] == '@':
            title = tweet
        else:
            title = '#%s' % tweet
    return title


def getImage(req):
    """ return the post media or choose image of the user profile """

    try:
        image_url = req['entities']['media'][0]['media_url']
    except KeyError:
        image_url = req['user']['profile_image_url']
    return image_url


def getDesc(req):
    """  Get the description """

    try:
        desc = req['text']
    except KeyError:
        desc = 'No description'
    return desc


def process(input, entities=None):
    """ process entities = ('twitter') """

    output = {}
    tweet = ""
    try:
        tweet = entities['twitter'][0]['value']
        url, req = getUrl(tweet)
        title = getTitle(req, tweet)
        image = getImage(req)
        desc = getDesc(req)
        template = GenericTemplate()
        buttons = ButtonTemplate()
        buttons.add_web_url('Read more...', url)
        template.add_element(item_url=url, title=title, image_url=image,
                             subtitle=desc, buttons=buttons.get_buttons())
        output['input'] = input
        output['output'] = template.get_message()
        output['success'] = True
    except Exception:
        if tweet:
            error_message = 'There was some error while retrieving Twitter for %s' % tweet
        else:
            error_message = 'It seems you specify any tweet to lookup for... Maybe try without #hashtag ?'
        output['error_msg'] = TextTemplate(error_message).get_message()
        output['success'] = False
    return output
