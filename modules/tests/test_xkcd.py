import modules


def test_xkcd():
    assert ('xkcd' == modules.process_query('xkcd comic')[0])
    assert ('xkcd' == modules.process_query('xkcd')[0])
    assert ('xkcd' != modules.process_query('something random')[0])
