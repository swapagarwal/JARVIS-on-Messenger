import modules


def test_book():
    assert ('book' == modules.process_query('book timeline')[0])
    assert ('book' == modules.process_query('have you read harry potter?')[0])
    assert ('book' == modules.process_query('little women book rating')[0])
    assert ('book' != modules.process_query('harry potter movie')[0])
    assert ('book' != modules.process_query('something random')[0])
