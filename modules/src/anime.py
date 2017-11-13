import requests
import requests_cache

from templates.button import *
from utils.YouTube import YouTubeUtil


def process(input, entities):
    output = {}
    try:
        anime = entities['anime'][0]['value']

        with requests_cache.enabled('anime_cache', backend='sqlite', expire_after=86400):
            r = requests.get('https://kitsu.io/api/edge/anime', params={
                'filter[text]': anime,
                'page[limit]': 1
            })
            data = r.json()

        top_anime = data['data'][0]['attributes']

        template = TextTemplate()
        template.set_text('Title: ' + top_anime['canonicalTitle'] + '\nSynopsis: ' + top_anime['synopsis'])
        template.set_post_text(
            '\nAverage Rating: {0}%\nPopularity Rank: {1}\nRating Rank: {2}\nEpisode Count: {3}'.format(
                top_anime['averageRating'], str(top_anime['popularityRank']), str(top_anime['ratingRank']),
                str(top_anime['episodeCount'])))
        text = template.get_text()

        template = ButtonTemplate(text)
        template.add_web_url('Kitsu URL', 'https://kitsu.io/anime/' + top_anime['slug'])
        template.add_web_url('YouTube URL', YouTubeUtil.get_video_url(top_anime['youtubeVideoId']))

        output['input'] = input
        output['output'] = template.get_message()
        output['success'] = True
    except:
        error_message = 'I couldn\'t find any anime matching your query.'
        error_message += '\nPlease ask me something else, like:'
        error_message += '\n  - Death Note anime'
        error_message += '\n  - Dragon ball super anime status'
        error_message += '\n  - What is the anime rating of One Punch Man?'
        output['error_msg'] = TextTemplate(error_message).get_message()
        output['success'] = False
    return output
