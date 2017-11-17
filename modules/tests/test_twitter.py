import modules


def test_twitter():
    assert ('twitter' == modules.process_query('Show me some recent tweets about Donald Trump')[0])
    assert ('twitter' == modules.process_query('Tweets about Donald Trump')[0])
    assert ('twitter' == modules.process_query('Twitter news about Donald Trump')[0])
    assert ('twitter' == modules.process_query('What\'s up on Twitter about Donald Trump')[0])
    assert ('twitter' != modules.process_query('Show me some songs')[0])
    assert ('twitter' != modules.process_query('Show me information about Donald Trump')[0])
