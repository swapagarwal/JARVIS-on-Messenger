import modules


def test_url():
    intent, entities = modules.process_query('shorten google.com')
    assert ('url' == intent)
    assert ('google.com' == entities['url'][0]['value'])
    assert ('shorten' == entities['url_action'][0]['value'])

    intent, entities = modules.process_query('give me a short version of bing.com')
    assert ('url' == intent)
    assert ('bing.com' == entities['url'][0]['value'])
    assert ('shorten' == entities['url_action'][0]['value'])

    intent, entities = modules.process_query('expand http://goo.gl/7aqe')
    assert ('url' == intent)
    assert ('http://goo.gl/7aqe' == entities['url'][0]['value'])
    assert ('expand' == entities['url_action'][0]['value'])

    assert ('url' != modules.process_query('something random')[0])
