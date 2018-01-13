import modules


def test_cocktail():
    assert ('cocktail' == modules.process_query('margarita cocktail')[0])
    assert ('cocktail' == modules.process_query('mai tai cocktail')[0])
    assert ('cocktail' == modules.process_query('cocktail martini')[0])
    assert ('cocktail' != modules.process_query('test')[0])
