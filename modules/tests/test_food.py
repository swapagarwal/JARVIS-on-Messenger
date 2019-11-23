import modules


def test_food():
    # test that Wit.ai is able to determine the intent of these queries as "food"
    assert ('food' == modules.process_query('food')[0])
    assert ('food' == modules.process_query('food menu')[0])
    assert ('food' == modules.process_query('what\s the food menu')[0])
    assert ('food' == modules.process_query('what should I eat?')[0])
    assert ('food' != modules.process_query('roll a die')[0])

    # test that JARVIS is able to produce the appropriate response
    assert (len(modules.search('food')) > 0)