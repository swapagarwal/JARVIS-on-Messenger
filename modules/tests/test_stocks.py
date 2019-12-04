import modules


def test_stocks():
    assert (('stocks', 'aapl') == modules.process_query('stock AAPL')[0])
    assert (('stocks', 'aapl') == modules.process_query('price of AAPL stock')[0])
    assert (('stocks', 'aapl') != modules.process_query('AAPL stock price')[0])
    assert (('stocks', 'aapl') != modules.process_query('MSFT stock price')[0])
    assert (('stocks', 'msft') != modules.process_query('MSFT stock price')[0])
    assert (('stocks', 'aapl') != modules.process_query('something random')[0])
