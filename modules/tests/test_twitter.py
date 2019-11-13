import modules


def test_news():

    assert ('twitter' == modules.process_query('twitter trend')[0])
    assert ('twitter' == modules.process_query('trending topics')[0])
    assert ('twitter' == modules.process_query('trending hashtags')[0])
    assert ('twitter' == modules.process_query('Newyork trends')[0])
    assert ('twitter' == modules.process_query('twitter trends worlwide')[0])
    assert ('twitter' == modules.process_query('trend in India')[0])
    assert ('twitter' == modules.process_query('trends in Mumbai')[0])
    assert ('twitter' != modules.process_query('something random')[0])
