import modules

def test_pick():
    assert('pick' == modules.process_query('pick chinese japanese indian')[0])
    assert('pick' == modules.process_query('pick 1 2 3')[0])
    assert('pick' == modules.process_query('pick a b c')[0])
    assert('pick' != modules.process_query('Death Note anime')[0])
