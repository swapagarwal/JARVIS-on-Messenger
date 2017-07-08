import modules


def test_request():
    assert ('request' == modules.process_query('request')[0])
    assert ('request' == modules.process_query('report')[0])
    assert ('request' != modules.process_query('something random')[0])
