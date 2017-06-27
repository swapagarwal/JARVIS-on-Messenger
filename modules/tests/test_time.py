import modules


def test_time():
    assert ('time' == modules.process_query('time in new york')[0])
    assert ('time' == modules.process_query('india time')[0])
    assert ('time' == modules.process_query('time at paris')[0])
    assert ('time' != modules.process_query('something random')[0])
