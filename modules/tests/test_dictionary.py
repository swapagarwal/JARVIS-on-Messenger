import modules


def test_dictionary():
    assert ('dictionary' == modules.process_query('define comfort')[0])
    assert ('dictionary' == modules.process_query('cloud definition')[0])
    assert ('dictionary' == modules.process_query('what does an accolade mean?')[0])
    assert ('dictionary' != modules.process_query('something random')[0])
