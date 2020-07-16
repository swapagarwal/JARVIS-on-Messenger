import modules

def test_worldcup():
    assert ('worldcup' == modules.process_query('when is the next match in the world cup')[0])
    assert ('worldcup' == modules.process_query('when are france playing again')[0])
