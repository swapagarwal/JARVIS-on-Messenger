import modules


def test_wiki():
    intent, entities = modules.process_query('wiki barack')
    assert ('wiki' == intent)
    assert ('barack' == entities['wiki'][0]['value'])

    assert ('wiki' == modules.process_query('html wiki')[0])
    assert ('wiki' == modules.process_query('who is sachin tendulkar')[0])
    assert ('wiki' != modules.process_query('joke definition')[0])
    assert ('wiki' != modules.process_query('something random')[0])
