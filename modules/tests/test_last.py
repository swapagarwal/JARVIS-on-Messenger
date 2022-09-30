import modules


def test_thanks():
    assert ('last' == modules.process_query('last')[0])
    assert ('last' == modules.process_query('BYE BYE')[0])
    assert ('last' != modules.process_query('Good BYE')[0])
