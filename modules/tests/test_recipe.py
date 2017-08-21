import modules


def test_recipe():
    assert ('recipe' == modules.process_query('chicken recipe')[0])
    assert ('recipe' == modules.process_query('random recipe')[0])
    assert ('recipe' == modules.process_query('recipe of roast potatoes')[0])
    assert ('recipe' != modules.process_query('something random')[0])
