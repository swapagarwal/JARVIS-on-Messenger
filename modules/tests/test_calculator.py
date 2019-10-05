import modules


def test_calculator():
    assert ('calculator' == modules.process_query('Calculate 3x4')[0])
    assert ('calculator' == modules.process_query('Calculate (5-3)x2')[0])
    assert ('calculator' == modules.process_query('Calculate 4/2')[0])
    assert ('calculator' != modules.process_query('something random')[0])
