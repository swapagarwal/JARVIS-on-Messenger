import modules


def test_joke():
    assert ('joke' == modules.process_query('tell me a joke')[0])
    assert ('joke' == modules.process_query('Do you know a joke?')[0])
    assert ('joke' == modules.process_query('random jokes')[0])
    assert ('joke' != modules.process_query('something random')[0])
