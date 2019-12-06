import modules


def test_urban():
    assert (('urban', 'lol') == modules.process_query('slang lol'))
    assert (('urban', 'lol') == modules.process_query('meaning of slang lol'))
    assert (('urban', 'lol') == modules.process_query('urban dictionary definition of slang lol'))
    assert (('urban', 'lol') != modules.process_query('something random'))