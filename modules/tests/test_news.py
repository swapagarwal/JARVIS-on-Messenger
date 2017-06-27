import modules


def test_news():
    assert ('news' == modules.process_query('news')[0])
    assert ('news' == modules.process_query('latest news')[0])
    assert ('news' == modules.process_query('world news')[0])
    assert ('news' != modules.process_query('something random')[0])
