import modules


def test_twitter():
    assert ('twitter' == modules.process_query('Show me some recent tweets about Donald Trump')[0])
    assert ('twitter' != modules.process_query('Show me some songs')[0])
