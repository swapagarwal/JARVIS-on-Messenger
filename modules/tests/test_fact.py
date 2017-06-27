import modules


def test_fact():
    assert ('fact' == modules.process_query('tell me a fact')[0])
    assert ('fact' == modules.process_query('Do you know a fact?')[0])
    assert ('fact' == modules.process_query('random facts')[0])
    assert ('fact' != modules.process_query('something random')[0])
