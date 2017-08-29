import modules


def test_food():
    assert ('food' == modules.process_query('Is Giordano\'s pizza in Chicago good?')[0])
    assert ('food' == modules.process_query('Chipotle in Evanston')[0])
    assert ('food' == modules.process_query('What are some restaurants in Chicago')[0])
    assert ('food' != modules.process_query('something random')[0])