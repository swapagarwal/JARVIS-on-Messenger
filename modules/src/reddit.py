import praw
import config
import os
from templates.button import *

REDDIT_CLIENT_ID = os.environ.get('REDDIT_CLIENT_ID', config.REDDIT_CLIENT_ID)
REDDIT_CLIENT_SECRET = os.environ.get('REDDIT_CLIENT_SECRET', config.REDDIT_CLIENT_SECRET)

def getTop(sub):
    reddit = praw.Reddit(user_agent='messenger-bot', client_id=REDDIT_CLIENT_ID ,client_secret=REDDIT_CLIENT_SECRET)
    submissions = reddit.subreddit(sub).top('day', limit=1)
    for submission in submissions:
        return([str(submission.title), str(submission.url), str(submission.score)])

def process(input, entities):
    sub = entities['sub'][0]['value']
    if sub[:2] == "r/":
        sub = sub[2:]
    try:
        result = getTop(sub)
        error = False
    except:
        error = True
        err_message = "Subreddit not found... Please try again.\nUsage: reddit [subreddit]"
    output = {}
    if not error:
        template = TextTemplate('Today\'s top post at r/ ' + sub + ':'
                                '\nTitle: ' + result[0] +
                                '\nUpvotes: ' + result[2])
        text = template.get_text()
        template = ButtonTemplate(text)
        template.add_web_url('View post', result[1])

        output['input'] = input
        output['output'] = template.get_message()
        output['success'] = True
    else:
        template = TextTemplate(err_message)
        output['input'] = input
        output['output'] =template.get_text()
        output['success'] = True

    return output
