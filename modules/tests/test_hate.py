import modules


def test_hate():
    assert('hate' == module.process_query('i hate you')[0])
    assert('hate' == module.process_query('Do you hate me?')[0])
    assert('hate' != module.process_query('something random')[0])
