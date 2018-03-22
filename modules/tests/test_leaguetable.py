import modules

def test_leaguetable():
    assert('leaguetable' == modules.process_query('Show me the Premier League Table')[0])
    assert('leaguetable' == modules.process_query('Show me Italian football team rankings')[0])
    assert('leaguetable' == modules.process_query('What is the Bundesliga football table?')[0])
    assert('leaguetable' != modules.process_query('something random')[0])