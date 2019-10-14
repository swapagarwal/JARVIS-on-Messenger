import modules

def test_cat_fact():
    assert ('cat_fact' == modules.process_query('tell me a cat fact')[0])
    assert ('cat_fact' == modules.process_query('Do you know a cat fact?')[0])
    assert ('cat_fact' == modules.process_query('random cat facts')[0])
    assert ('cat_fact' != modules.process_query('something random')[0])
