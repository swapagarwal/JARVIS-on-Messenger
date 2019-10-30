import modules


def test_hate():
    assert('hate' == modules.process_query('i hate you')[0])
    assert('hate' == modules.process_query('Do you hate me?')[0])
    assert('hate' != modules.process_query('something random')[0])
