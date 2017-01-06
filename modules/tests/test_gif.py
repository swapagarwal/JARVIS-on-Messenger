import modules

def test_gif():
    assert('gif' == modules.process_query('cat gifs')[0])
    assert('gif' == modules.process_query('gif of laughing children')[0])
    assert('gif' == modules.process_query('a southpark gif')[0])
    assert('gif' == modules.process_query('JARVIS, could you hand me a gif of funny cats?')[0])
    assert('gif' != modules.process_query('something random')[0])
