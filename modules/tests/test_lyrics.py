import modules


def test_lyrics():
    assert ('lyrics' == modules.process_query('paradise lyrics')[0])
    assert ('lyrics' == modules.process_query('lyrics of the song hall of fame')[0])
    assert ('lyrics' == modules.process_query('What are the lyrics to see you again?')[0])
    assert ('lyrics' != modules.process_query('something random')[0])
