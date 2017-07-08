import modules


def test_bye():
    assert ('bye' == modules.process_query('bye')[0])
    assert ('bye' == modules.process_query('good night')[0])
    assert ('bye' != modules.process_query('something random')[0])
