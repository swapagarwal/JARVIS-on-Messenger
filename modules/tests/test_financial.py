import modules


def test_news():
    assert ('financial' == modules.process_query('financial')[0])
    assert ('financial' == modules.process_query('financial news')[0])
    assert ('financial' == modules.process_query('economic news')[0])
    assert ('financial' != modules.process_query('something random')[0])