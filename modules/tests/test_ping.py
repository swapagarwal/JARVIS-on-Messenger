import modules

def test_ping():
    assert ('ping' == modules.process_query('ping google.com')[0])
    assert ('ping' == modules.process_query('ping')[0])
    assert ('ping' != modules.process_query('something random')[0])

    
