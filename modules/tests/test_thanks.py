import modules


def test_thanks():
    assert ('thanks' == modules.process_query('thanks')[0])
    assert ('thanks' == modules.process_query('thank you')[0])
    assert ('thanks' != modules.process_query('something random')[0])
