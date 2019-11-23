import modules


def test_equity():
    assert ('equity' == modules.process_query('What is the stock price of MSFT?')[0])
    assert ('equity' == modules.process_query('GOOG close price')[0])
    assert ('equity' == modules.process_query('Last closing price for AAPL')[0])
    assert ('equity' != modules.process_query('LYFT stock')[0])
