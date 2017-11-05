import modules


def test_hello():
    assert ('love' == modules.process_query('I love you')[0])
    assert ('love' == modules.process_query('I like you')[0])
    assert ('love' == modules.process_query('I missed you')[0])
    assert ('love' == modules.process_query('Do you love me?')[0])
    assert ('love' != modules.process_query('something random')[0])
