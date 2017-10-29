import modules


def test_reddit():
    intent, entities = modules.process_query('reddit dankmemes')
    assert ('reddit' == intent)
    assert ('dankmemes' == entities['sub'][0]['value'])

    intent, entities = modules.process_query('sub dankmemes')
    assert ('reddit' == intent)
    assert ('dankmemes' == entities['sub'][0]['value'])

    intent, entities = modules.process_query('subreddit dankmemes')
    assert ('reddit' == intent)
    assert ('dankmemes' == entities['sub'][0]['value'])

    assert ('reddit' != modules.process_query('something random')[0])
