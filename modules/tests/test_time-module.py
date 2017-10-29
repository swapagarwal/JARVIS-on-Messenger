import modules


def test_time-module():
    assert ('time-module' == modules.process_query('time in new york')[0])
    assert ('time-module' == modules.process_query('india time')[0])
    assert ('time-module' == modules.process_query('time at paris')[0])
    assert ('time-module' != modules.process_query('something random')[0])
