import modules

def test_cat_fact():
    assert ('cat_fact' == modules.process_query('I am very bored')[0])
    assert ('cat_fact' == modules.process_query('Tell me something to do')[0])
    assert ('cat_fact' == modules.process_query('what should I do now?')[0])
    assert ('cat_fact' != modules.process_query('tell me some activities')[0])
