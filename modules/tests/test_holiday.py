import modules


def test_holiday():
    assert ('holiday' == modules.process_query('what is the nearest holiday?')[0])
    assert ('holiday' != modules.process_query('something random')[0])