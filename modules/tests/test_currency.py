import modules

def test_currency():
    assert('currency' == modules.process_query('HKD to USD')[0])
    assert('currency' == modules.process_query('USD to INR')[0])
    assert('currency' == modules.process_query('how much is USD in EUR')[0])
    assert('currency' != modules.process_query('something random')[0])
