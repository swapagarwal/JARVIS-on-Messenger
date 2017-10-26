import modules


def test_pick():
    assert ('pick' == modules.process_query('pick pasta tacos pizza')[0])
    intent, entities = modules.process_query('pick blade runner, the shining, the godfather')
    assert ('pick' == intent)
    assert ('blade runner, the shining, the godfather' == entities['pick'][0]['value'])
    assert ('pick' != modules.process_query('something random')[0])
