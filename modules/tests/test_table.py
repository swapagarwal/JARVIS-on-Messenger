import modules


def test_coin():
    assert ('table' == modules.process_query('Flip a table')[0])
    assert ('table' == modules.process_query('I hate tables')[0])
    assert ('table' == modules.process_query('Can you flip a table?')[0])
    assert ('table' != modules.process_query('something random')[0])
