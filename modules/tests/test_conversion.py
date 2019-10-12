import modules


def test_conversion():
    assert ('conversion' == modules.process_query('convert 50 kg to pounds')[0])
    assert ('conversion' == modules.process_query('what is 20 C in F')[0])
    assert ('conversion' == modules.process_query('100 m in feet')[0])
    assert ('conversion' == modules.process_query('5 inches to mm')[0])

    intent, entities = modules.process_query('convert 50 kg to pounds')
    assert ('conversion' == intent)
    assert ('kg' == entities['from_unit'][0]['value'])
    assert ('pounds' == entities['to_unit'][0]['value'])
    assert (50 == entities['number'][0]['value'])

    intent, entities = modules.process_query('what is 20 C in F')
    assert ('conversion' == intent)
    assert ('C' == entities['from_unit'][0]['value'])
    assert ('F' == entities['to_unit'][0]['value'])
    assert (20 == entities['number'][0]['value'])

    assert ('conversion' != modules.process_query('something random')[0])