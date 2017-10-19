from random import randint
import praw
import modules
from templates.generic import *

#aww pulls top 25 posts from reddit.com/r/aww and serves the receipient a random image
def process(input, entities):
    output = {}

    reddit = praw.Reddit(client_id='hidrsV8C-QzMmQ',
                         client_secret='segvJkUHCUFquxCxqz5ml9-tlmE',
                         user_agent='JARVIS_ON_MESSENGER module by u/argfooiv')

    subreddit = reddit.subreddit('aww')
    posts = []

    #request returns top 25 posts from r/aww
    #skipping indicie 0 due to reddit announcements 
    r = randint(1, 24)

    for index, submission in enumerate(subreddit.hot(limit=25)):
        posts.append(submission)

    post_title =  posts[r].title
    post_url = posts[r].url

    template = GenericTemplate()
    template.set_image_aspect_ratio_to_square()
    template.add_element(title=post_title, image_url=post_url)

    message = template.get_message()

    output = {
        'input': input,
        'output': message,
        'success': True
    }

    return output
