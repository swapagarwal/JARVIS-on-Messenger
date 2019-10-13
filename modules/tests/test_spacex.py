import modules


def test_book():
    assert ('spacex' == modules.process_query('next spacex launch')[0])
    assert ('spacex' != modules.process_query('something random')[0])
