import modules

def test_cricket():
    assert ('cricket' == modules.process_query('cricket')[0])
    assert ('cricket' == modules.process_query('live cricket')[0])
    assert ('cricket' == modules.process_query('cricket livescores')[0])
    assert ('cricket' != modules.process_query('something random')[0])

