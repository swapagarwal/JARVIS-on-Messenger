import modules


def test_cocktail():
    assert ('cocktail' == modules.process_query('margarita cocktail')[0])
    assert ('cocktail' == modules.process_query('mai tai cocktail')[0])
    assert ('cocktail' == modules.process_query('manhattan cocktail')[0])
    assert ('cocktail' != modules.process_query('something random')[0])
