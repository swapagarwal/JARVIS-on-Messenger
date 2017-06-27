import modules


def test_music():
    assert ('music' == modules.process_query('hymn for the weekend song')[0])
    assert ('music' == modules.process_query('linkin park songs')[0])
    assert ('music' == modules.process_query('play hotel california')[0])
    assert ('music' != modules.process_query('something random')[0])
