import modules


def test_coin():
    assert ('coin' == modules.process_query('Flip a coin')[0])
    assert ('coin' == modules.process_query('heads or tails')[0])
    assert ('coin' == modules.process_query('Can you flip a coin?')[0])
    assert ('coin' != modules.process_query('something random')[0])
