import modules

def test_anime():
    assert('anime' == modules.process_query('Death Note anime')[0])
    assert('anime' == modules.process_query('Dragon ball super status')[0])
    assert('anime' == modules.process_query('What is the rating of One Punch Man?')[0])
    assert('anime' != modules.process_query('something random')[0])
