import modules


def test_sports():
    assert ('world cup' == modules.process_query('France 2018 World Cup')[0])
    assert ('world cup' == modules.process_query('germany 2018 fifa world cup results')[0])
    assert ('world cup' == modules.process_query('How did Mexico do in the 2018 FIFA World Cup?')[0])
    assert ('world cup' != modules.process_query('something random')[0])