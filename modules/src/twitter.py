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
        message = 'Okay, here are some tweets about ' + keyword + '<br><br>' + response.encode('ascii', 'xmlcharrefreplace')
        output['input'] = input
        output['output'] = message
        output['success'] = True
    except:
        output['success'] = False
    return output


def api_search(keyword):

    ts = TwitterSearch(
        consumer_key=TWITTER_CONSUMER_KEY,
        consumer_secret=TWITTER_CONSUMER_SECRET,
        access_token=TWITTER_ACCESS_TOKEN,
        access_token_secret=TWITTER_ACCESS_TOKEN_SECRET
    )

    tuoFilter = TwitterUserOrder("JARVIS")
    tuoFilter.set_exclude_replies(True)
    tuoFilter.set_include_rts(False)
    tuoFilter.set_contributor_details(False)

    tsoFilter = TwitterSearchOrder() # create a TwitterSearchOrder object
    tsoFilter.set_keywords([keyword])
    tsoFilter.set_language('en')
    tsoFilter.set_count(3)
    tsoFilter.set_include_entities(False) # and don't give us all those entity information

    tso = TwitterSearchOrder()
    tso.set_search_url(tsoFilter.create_search_url() + tuoFilter.create_search_url())

    result = ''
    counter = 0

    results = ts.search_tweets(tsoFilter)

    for tweet in results['content']['statuses']:
        result += tweet['user']['screen_name'] + ' tweeted: ' + tweet['text'] + "<br><br>"
        print('@%s tweeted: %s' % (tweet['user']['screen_name'], tweet['text']))

    return result