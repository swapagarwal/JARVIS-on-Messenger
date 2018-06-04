import modules

def test_place():
    assert ('place' == modules.process_query('give me a place')[0])
    assert ('place' == modules.process_query('I want to go on a trip')[0])
    assert ('place' != modules.process_query('something random')[0])
