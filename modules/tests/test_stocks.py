import modules


def test_stock():
    assert ('stocks' == modules.process_query('What is the price of apple?')[0])
    assert ('stocks' == modules.process_query('price of apple')[0])
    assert ('stocks' == modules.process_query('what does apple cost?')[0])
    assert ('stocks' != modules.process_query('something random')[0])
