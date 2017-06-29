import modules
import json


def test_anime():
    assert ('anime' == modules.process_query('Death Note anime')[0])
    assert ('anime' == modules.process_query('Dragon ball super anime status')[0])
    assert ('anime' == modules.process_query('What is the anime rating of One Punch Man?')[0])
    assert ('anime' != modules.process_query('something random')[0])

    response = modules.search('Death Note anime')
    response_payload = response['attachment']['payload']
    
    # Test that a payload was returned as a string

    assert(type(response_payload['text']) is str 
            or type(response_payload is unicode))

    # Test that the expected title was returned

    expected_title = 'Title: Death Note'
    assert(response_payload['text'][:len(expected_title)] == expected_title)

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

    # Test a bad query to ensure the error is handled gracefully

    bad_search = '?!>< anime'
    expected_error = "I couldn't find any anime matching your query"

    response = modules.search(bad_search)

    assert('anime' == modules.process_query('?!>< anime')[0])
    assert('text' in response)
    assert(len(response['text']) >= len(expected_error))
    assert(response['text'][:len(expected_error)] == expected_error)
