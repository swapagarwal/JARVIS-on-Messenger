import modules


def test_wiki():
    assert ('wiki' == modules.process_query('wikipedia barack')[0])
    assert ('wiki' == modules.process_query('html wiki')[0])
    assert ('wiki' == modules.process_query('who is sachin tendulkar')[0])
    assert ('wiki' != modules.process_query('joke definition')[0])
    assert ('wiki' != modules.process_query('something random')[0])
