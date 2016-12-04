import modules

def test_xkcd():
    assert('xkcd' == modules.process_query('Show me the latest xkcd')[0])
    assert('xkcd' == modules.process_query('current xkcd')[0])
    assert('xkcd' == modules.process_query('show me an xkcd')[0])
    assert('xkcd' != modules.process_query('tell me a joke')[0])
