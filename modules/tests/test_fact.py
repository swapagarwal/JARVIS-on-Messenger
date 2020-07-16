import modules
import config
import json

# The number of quick replies added to the module
NUM_QUICK_REPLIES = 3


def test_intents():

    assert ('fact' == modules.process_query('tell me a fact')[0])
    assert ('fact' == modules.process_query('Do you know a fact?')[0])
    assert ('fact' == modules.process_query('random facts')[0])
    assert ('fact' != modules.process_query('something random')[0])


def test_payload():

    # Make sure a string is returned.
    response = modules.search('tell me a fact')
    assert ('text' in response)

    # Make sure the result was a line from the data file, not an error.
    with open(config.FACTS_SOURCE_FILE) as facts_file:
        facts_list = json.load(facts_file)
        assert (type(response['text']) is str
                or type(response['text'] is unicode))
        assert (response['text'] in facts_list['facts'])


def test_quick_replies():

    response = modules.search('tell me a fact')

    # Test for quick replies being present
    assert('quick_replies' in response)

    # Test for expected number of quick replies
    reply_list = response['quick_replies']
    assert(len(reply_list) == NUM_QUICK_REPLIES)

    # Test for expected quick reply intents
    expected_replies = ["fact", "joke", "quote"]

    '''Check the reply's payload for the string stating the
    reply's intent. Attempt to remove the reply from the
    list of replies.'''
    for reply in reply_list:
        extracted = json.loads(reply['payload'])
        expected_replies.remove(extracted['intent'])

    '''If the replies list contained all of the
    expected replies and only the expected replies,
    expected replies should now be empty.'''
    assert(len(expected_replies) == 0)
