import modules

def test_cpcontest():
    assert('cpcontest' == modules.process_query('upcoming contests')[0])
    assert('cpcontest' == modules.process_query('programming contests')[0])
    assert('cpcontest' != modules.process_query('something random')[0])
