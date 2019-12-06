import modules


def test_love():
    assert ('love' == modules.process_query('i love you')[0])
    assert ('love' == modules.process_query('i like you')[0])
    assert ('love' == modules.process_query('do you love me')[0])
    assert ('love' == modules.process_query('do you like me')[0])
    assert ('love' == modules.process_query('what is love?')[0])
    assert ('love' != modules.process_query('something random')[0])
    assert ('love' != modules.process_query('Love is an open door')[0])
