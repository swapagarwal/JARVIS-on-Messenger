import os
import config

import requests
import requests_cache

from TwitterSearch import *

TWITTER_CONSUMER_KEY = os.environ.get('TWITTER_CONSUMER_KEY', config.TWITTER_CONSUMER_KEY)
TWITTER_CONSUMER_SECRET = os.environ.get('TWITTER_CONSUMER_SECRET', config.TWITTER_CONSUMER_SECRET)
TWITTER_ACCESS_TOKEN = os.environ.get('TWITTER_ACCESS_TOKEN', config.TWITTER_ACCESS_TOKEN)
TWITTER_ACCESS_TOKEN_SECRET = os.environ.get('TWITTER_ACCESS_TOKEN_SECRET', config.TWITTER_ACCESS_TOKEN_SECRET)

def process(input, entities=None):
    keyword = None
    if entities is not None and len(entities) > 0:
        keyword = entities[0]["value"]

    if keyword is None:
        keyword = "news"

    output = {}
    try:
        response = None
        response = api_search(keyword)
        message = "Okay, here are some tweets about " + keyword + "<br><br>" + response
        output['input'] = input
        output['output'] = message
        output['success'] = True
    except:
        output['success'] = False
    return output


def api_search(keyword):
    try:
        tso = TwitterSearchOrder() # create a TwitterSearchOrder object
        tso.set_keywords([keyword])
        tso.set_language('en')
        tso.set_count(1)
        tso.set_include_entities(False) # and don't give us all those entity information

        tuo = TwitterUserOrder("JARVIS")
        tuo.set_exclude_replies(True)

        # it's about time to create a TwitterSearch object with our secret tokens
        ts = TwitterSearch(
            consumer_key = TWITTER_CONSUMER_KEY,
            consumer_secret = TWITTER_CONSUMER_SECRET,
            access_token = TWITTER_ACCESS_TOKEN,
            access_token_secret = TWITTER_ACCESS_TOKEN_SECRET
         )

        result = ""

         # this is where the fun actually starts :)
        for tweet in ts.search_tweets_iterable(tso):
            result += tweet['user']['screen_name'] + ' tweeted: ' + tweet['text'] + "<br><br>"
            print( '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ) )

    except TwitterSearchException as e: # take care of all those ugly errors if there are some
        print(e)

    return result