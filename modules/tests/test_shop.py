import modules


def test_music():
    assert ('shop' == modules.process_query('buy remote control')[0])
    assert ('shop' == modules.process_query('I need toilet paper')[0])
    assert ('shop' == modules.process_query('purchase television')[0])
    assert ('shop' != modules.process_query('something random')[0])
