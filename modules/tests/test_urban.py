import modules

def test_urban():
    assert('urban' == modules.process_query('urban lol')[0])
    assert('urban' == modules.process_query('lol urban')[0])
    assert('urban' == modules.process_query('slang lol')[0])
    assert('urban' != modules.process_query('something random')[0])
