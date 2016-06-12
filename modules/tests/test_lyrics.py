import modules

def test_lyrics():
    assert('lyrics' == modules.process_query('chop him down with the edge of my hand lyrics')[0])
    assert('lyrics' == modules.process_query('lyrics you used to call me on my cellphone')[0])
    assert('lyrics' == modules.process_query('dark side of the moon lyrics')[0])
    assert('lyrics' != modules.process_query('lyrics black dog')[0])
