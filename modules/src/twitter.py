import os
import config
import urllib

from birdy.twitter import UserClient
from templates.text import *

TWITTER_CONSUMER_KEY = os.environ.get('TWITTER_CONSUMER_KEY', config.TWITTER_CONSUMER_KEY)
TWITTER_CONSUMER_SECRET = os.environ.get('TWITTER_CONSUMER_SECRET', config.TWITTER_CONSUMER_SECRET)
TWITTER_ACCESS_TOKEN = os.environ.get('TWITTER_ACCESS_TOKEN', config.TWITTER_ACCESS_TOKEN)
TWITTER_ACCESS_TOKEN_SECRET = os.environ.get('TWITTER_ACCESS_TOKEN_SECRET', config.TWITTER_ACCESS_TOKEN_SECRET)

CHARACTER_LIMIT = 1024


def process(input, entities=None):
    keyword = None
    if entities is not None and len(entities) > 0:
        keyword = entities[0]["value"]

    if keyword is None:
        keyword = "news"

    output = {}
    try:
        response = api_search(keyword)
        message = TextTemplate()
        output_text = 'Okay, here are some tweets about ' + keyword + '\n\n' + response.encode('ascii',
                                                                                                   'xmlcharrefreplace')
        message.set_text(text=output_text)
        message.set_post_text('')
        message.set_limit(CHARACTER_LIMIT)

        output['input'] = input
        output['output'] = message.get_message()
        output['success'] = True
    except:
        output['success'] = False
    return output


def api_search(keyword):
    client = UserClient(TWITTER_CONSUMER_KEY,
                        TWITTER_CONSUMER_SECRET,
                        TWITTER_ACCESS_TOKEN,
                        TWITTER_ACCESS_TOKEN_SECRET)

    keyword = urllib.quote(keyword.encode('utf8'))
    response = client.api.search.tweets.get(q=keyword, count=3, tweet_mode='extended')
    result = ""
    for tweet in response.data['statuses']:
        link = 'https://twitter.com/%s/status/%s' % (tweet['user']['screen_name'], tweet['id'])
        link = '<a href=' + link + '>Show in Twitter</a>'
        result += tweet['user']['name'] + ' tweeted: ' + tweet['full_text'] + ' ' + link + '\n\n'

    return result
