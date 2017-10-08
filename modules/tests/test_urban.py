import modules


def test_urban():
    intent, entities = modules.process_query('urban rawr')
    assert ('urban' == intent)
    assert ('rawr' == entities[0]['word'])

    intent, entities = modules.process_query('rawr urban')
    assert ('urban' == intent)
    assert ('rawr' == entities[0]['word'])

    intent, entities = modules.process_query('slang rawr')
    assert ('urban' == intent)
    assert ('rawr' == entities[0]['word'])

    intent, entities = modules.process_query('rawr slang')
    assert ('urban' == intent)
    assert ('rawr' == entities[0]['word'])
