import modules

def test_lyrics():
    assert('lyrics' == modules.process_query("Lyrics for the song 'Wish you were here' ")[0])
    assert('lyrics' == modules.process_query("lyrics for 'Go Robot' ")[0])
    assert('lyrics' == modules.process_query("lyrics for the song Strawberry Fields Forever ")[0])
    assert('lyrics' != modules.process_query("something random")[0])
