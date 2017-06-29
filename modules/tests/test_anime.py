import modules
import json


def test_intents():
    assert ('anime' == modules.process_query('Death Note anime')[0])
    assert ('anime' == modules.process_query('Dragon ball super anime status')[0])
    assert ('anime' == modules.process_query('What is the anime rating of One Punch Man?')[0])
    assert ('anime' != modules.process_query('something random')[0])

    

def test_payload():

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

def test_bad():

    # Test a bad query to ensure the error is handled gracefully

    bad_search = '?!>< anime'
    assert('anime' == modules.process_query(bad_search)[0])

    # This will cause the test to fail if any exceptions are raised.
    response = modules.search(bad_search)
    assert('text' in response)    
