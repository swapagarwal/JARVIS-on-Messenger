import modules 

def test_webcheck():
    assert('webcheck' == modules.process_query('is google.com up')[0])
    assert('webcheck' == modules.process_query('google.com status')[0])
    assert('webcheck' != modules.process_query('something random')[0])
