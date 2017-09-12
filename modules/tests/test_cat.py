import modules


def test_coin():
    assert ('cat' == modules.process_query('cat')[0])
    assert ('cat' != modules.process_query('something random')[0])
