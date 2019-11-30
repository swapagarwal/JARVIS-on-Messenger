import modules

def test_fortune():
    assert (len(modules.search('fortune')) > 0)
    assert ('fortune' == modules.process_query('fortune')[0])
    assert ('fortune' == modules.process_query('fortune cookie')[0])
    assert ('fortune' == modules.process_query('open fortune cookie')[0])
    assert ('fortune' == modules.process_query('what is my fortune?')[0])
    assert ('fortune' == modules.process_query('what is my fortune for today?')[0])
    assert ('fortune' != modules.process_query('roll a die')[0])

