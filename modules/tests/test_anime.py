import modules
import json
import requests
import requests_cache
import random

TEST_TITLES = ['Death Note', 'One Punch Man', 'Dragon Ball Super',
        'Miss Kobayashi\'s Dragon Maid', 'Sailor Moon', 'Attack on Titan']

random.shuffle(TEST_TITLES)

def test_intents():
    assert ('anime' == modules.process_query('Death Note anime')[0])
    assert ('anime' == modules.process_query('Dragon ball super anime status')[0])
    assert ('anime' == modules.process_query('What is the anime rating of One Punch Man?')[0])
    assert ('anime' != modules.process_query('something random')[0])

def get_title_from_api(title):
    r = requests.get('https://kitsu.io/api/edge/anime', params={'filter[text]' : title,
        'page[limit]' : 1})
    data = r.json()
    expected_title = data['data'][0]['attributes']['canonicalTitle']

    return expected_title


def get_average_rating_from_api(title):
    r = requests.get('https://kitsu.io/api/edge/anime', params={'filter[text]' : title,
        'page[limit]' : 1})
    data = r.json()
    expected_rating = data['data'][0]['attributes']['averageRating']

    return expected_rating


def test_titles():
    for title in TEST_TITLES:

        response = modules.search(title + ' anime')
        response_payload = response['attachment']['payload']

        # Test that a payload was returned as a string

        assert(type(response_payload['text']) is str
                or type(response_payload is unicode))

        # Test that the expected title was returned

        expected_title = get_title_from_api(title)

        assert(response_payload['text'].startswith('Title: ' + expected_title))

        # Test that an average rating was returned

        assert('Average Rating: ' in response_payload['text'])

        # Test that a popularity rank was returned

        assert('Popularity Rank: ' in response_payload['text'])

        # Test that an episode count was returned

        assert('Episode Count: ' in response_payload['text'])

        payload_buttons = response_payload['buttons']

        # Test that a Kitsu URL was returned

        assert('url' in payload_buttons[0].keys())
        assert('https://kitsu.io' in payload_buttons[0]['url'])
        assert('title' in payload_buttons[0].keys())
        assert(payload_buttons[0]['title'] == "Kitsu URL")

        # Test that a YouTube URL was returned

        assert('url' in payload_buttons[1].keys())
        assert('https://www.youtube.com' in payload_buttons[1]['url'])
        assert('title' in payload_buttons[1].keys())
        assert(payload_buttons[1]['title'] == "YouTube URL")


def test_bad():

    # Test a bad query to ensure the error is handled gracefully

    bad_search = '?!>< anime'
    assert('anime' == modules.process_query(bad_search)[0])

    # This will cause the test to fail if any exceptions are raised.

    response = modules.search(bad_search)
    assert('text' in response)


def test_average_rating():

    for title in TEST_TITLES:

        response = modules.search(title + ' anime')
        response_payload = response['attachment']['payload']

        # Test that the average rating is a decimal percentage

        synopsis = response_payload['text']
        '''Parse the payload text, tokenizing by newlines.'''
        tokens = synopsis.split('\n')

        '''Find the token that begins with 'Average Rating: '''
        sought_token = 0
        current_token = 0
        while sought_token == 0:
            checked_token = tokens[current_token]
            if checked_token.startswith('Average Rating: '):
           
               '''Set the sought token flag to exit the loop'''
               sought_token = 1

               '''Remove the title.'''
               rating_token = checked_token.replace('Average Rating: ', '')

               decimal_points = 0
               percent_signs = 0

               '''Test that the value of the rating is correct based
               on the API's response.'''

               expected_rating = get_average_rating_from_api(title)
               response_rating = rating_token.replace('%', '')
               assert(float(expected_rating) == float(response_rating))

               '''Each character in the number string should be
               a digit, a decimal, or a percent sign.'''
               for character in rating_token:
                   assert(character.isdigit() or character == '.'
                           or character == '%')
                   if character == '.':
                       decimal_points += 1
                   elif character == '%':
                       percent_signs += 1

               '''Test that there is exactly one decimal and exactly
               one percent sign.'''
               assert(decimal_points == 1 and percent_signs == 1)

               '''Further split the token on the decimal sign to get
               the truncated whole number and ensure it is 
               between 0% and 100% (inclusive.)'''
               value_token = rating_token.split('.')[0]
               value_token = int(value_token)
               assert(value_token >= 0 and value_token <= 100)

               '''Test that the whole value, including the decimal part, is
               less than or equal to 100% by making sure if the whole
               number part is 100, the decimal part is exactly zero.'''
               if value_token == 100:

                   '''Get the decimal part by splitting on the decimal point
                   and taking the second token, then dropping the percent sign.'''
                   decimal_token = rating_token.split('.')[1]
                   decimal_token.replace('%', '')
                   decimal_token = int(decimal_token)
                   assert(decimal_token == 0)

            else:
               current_token += 1

'''
def test_popularity_rank():

    response = modules.search(TEST_TITLE + ' anime')
    response_payload = response['attachment']['payload']

    # Test that the popularity rank is an integer

    synopsis = response_payload['text']
    tokens = synopsis.split('\n')


    for token in tokens:
        if token.startswith('Popularity Rating: '):
'''
