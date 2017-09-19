import modules


def test_movie():
    assert ('movie' == modules.process_query('batman movie')[0])
    assert ('movie' == modules.process_query('iron man 2 movie plot')[0])
    assert ('movie' == modules.process_query('What is the rating of happyness movie?')[0])
    assert ('movie' != modules.process_query('something random')[0])
