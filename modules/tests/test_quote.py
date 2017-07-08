import modules


def test_quote():
    assert ('quote' == modules.process_query('quote')[0])
    assert ('quote' == modules.process_query('random quote')[0])
    assert ('quote' == modules.process_query('give me a quote')[0])
    assert ('quote' != modules.process_query('something random')[0])
