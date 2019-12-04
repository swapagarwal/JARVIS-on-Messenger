import modules


def test_crypto():
    assert (('crypto', 'btc') == modules.process_query('crpyto btc')[0])
    assert (('crypto', 'btc') == modules.process_query('btc crypto price')[0])
    assert (('crypto', 'btc') == modules.process_query('crypto btc price')[0])
    assert (('crypto', 'btc') == modules.process_query('price of btc crypto')[0])
    assert (('crypto', 'eth') == modules.process_query('crypto eth')[0])
    assert (('crypto', 'btc') != modules.process_query('something random')[0])
