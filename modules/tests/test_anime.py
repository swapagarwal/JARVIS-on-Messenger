import modules
import requests
import random

''' Shuffling the list of test titles allows us to ensure
the module is not just anticipating the test and giving a
canned response. These titles can be changed to any title
that returns an anime from the API.'''

TEST_TITLES = ['One Punch Man', 'Dragon Ball Super', 'Dragon Ball Z',
               'Sailor Moon', 'Attack on Titan', 'Bananya',
               'Jojo\'s Bizzare Adventure']

random.shuffle(TEST_TITLES)


def get_data_from_api(title):
    r = requests.get('https://kitsu.io/api/edge/anime', params={'filter[text]' : title,
                    'page[limit]' : 1})
    data = r.json()

    return data


def get_title_from_data(title):
    expected_title = get_data_from_api(title)['data'][0]['attributes']['canonicalTitle']
    return expected_title


def get_average_rating_from_data(title):
    expected_rating = get_data_from_api(title)['data'][0]['attributes']['averageRating']
    return expected_rating


def get_popularity_rank_from_data(title):
    expected_rank = get_data_from_api(title)['data'][0]['attributes']['popularityRank']
    return expected_rank


def get_episode_count_from_data(title):
    expected_count = get_data_from_api(title)['data'][0]['attributes']['episodeCount']
    return expected_count


def get_kitsu_link_from_data(title):
    expected_url = ('https://kitsu.io/anime/' +
                   get_data_from_api(title)['data'][0]['attributes']['slug'])

    return expected_url


def get_youtube_link_from_data(title):
    expected_url = ('https://www.youtube.com/watch?v=' +
                    get_data_from_api(title)['data'][0]['attributes']['youtubeVideoId'])

    return expected_url


def test_intents():
    assert ('anime' == modules.process_query('Death Note anime')[0])
    assert ('anime' == modules.process_query('Dragon ball super anime status')[0])
    assert ('anime' == modules.process_query('What is the anime rating of One Punch Man?')[0])
    assert ('anime' != modules.process_query('something random')[0])


def test_payloads(capsys):
    for title in TEST_TITLES:

        response = modules.search(title + ' anime')
        response_payload = response['attachment']['payload']

        # Test that a payload was returned as a string

        assert(type(response_payload['text']) is str
               or type(response_payload is unicode))

        # Test that the expected title was returned

        expected_title = get_title_from_data(title)

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
        current_token = 0
        while not (tokens[current_token].startswith('Average Rating: ')):
            current_token += 1

        checked_token = tokens[current_token]

        '''Remove the title.'''
        rating_token = checked_token.replace('Average Rating: ', '')

        decimal_points = 0
        percent_signs = 0

        '''Test that the value of the rating is correct based
        on the API's response.'''

        expected_rating = get_average_rating_from_data(title)
        response_rating = rating_token.split('%')[0]
        assert(expected_rating == response_rating)

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
            and taking the second token, then dropping the percent
            sign.'''
            decimal_token = rating_token.split('.')[1]
            decimal_token.replace('%', '')
            assert(int(decimal_token) == 0)


def test_popularity_rank():

    for title in TEST_TITLES:

        response = modules.search(title + ' anime')
        response_payload = response['attachment']['payload']

        # Test that the popularity rank is an integer

        synopsis = response_payload['text']
        tokens = synopsis.split('\n')

        '''Find the token that begins with Popularity Rank: '''
        current_token = 0

        while not (tokens[current_token].startswith('Popularity Rank: ')):
            current_token += 1

        checked_token = tokens[current_token]

        '''Remove the title.'''
        rating_token = checked_token.replace('Popularity Rank: ', '')

        '''The ranking should be a positive, non-zero integer.'''
        rank_value = int(rating_token)
        assert(rank_value > 0)

        '''Test that the value of the rank is correct based
        on the API's response.'''

        expected_rank = get_popularity_rank_from_data(title)
        assert(int(rating_token) == int(expected_rank))


def test_episode_count():

    for title in TEST_TITLES:

        response = modules.search(title + ' anime')
        response_payload = response['attachment']['payload']

        # Test that the episode count is an integer

        synopsis = response_payload['text']
        tokens = synopsis.split('\n')

        '''Find the token that begins with Episode Count: '''

        current_token = 0

        while not (tokens[current_token].startswith('Episode Count: ')):
            current_token += 1
        checked_token = tokens[current_token]

        '''Remove the title.'''
        count_token = checked_token.replace('Episode Count: ', '')

        '''The count should be a positive integer, or the
        string None.'''

        if count_token != "None":
            assert(int(count_token) > 0)

            '''Test that the value of the count is correct based
            on the API's response.'''

            expected_count = get_episode_count_from_data(title)
            assert(count_token == str(expected_count))


def test_kitsu_link():

    for title in TEST_TITLES:

        response = modules.search(title + ' anime')
        response_url = response['attachment']['payload']['buttons'][0]['url']

        assert(response_url == get_kitsu_link_from_data(title))


def test_youtube_link():

    for title in TEST_TITLES:

        response = modules.search(title + ' anime')
        response_url = response['attachment']['payload']['buttons'][1]['url']

        assert(response_url == get_youtube_link_from_data(title))
