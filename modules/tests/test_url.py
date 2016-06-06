import modules

def test_utl():
    assert('url' == modules.process_query('help shorten google.com')[0])
    assert('url' == modules.process_query('google.com shortener')[0])
    assert('url' == modules.process_query('give me a short version of google.com')[0])
    assert('url' != modules.process_query('something random')[0])
