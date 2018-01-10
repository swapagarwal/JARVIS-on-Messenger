import modules


def test_cocktail():
    assert ('cocktail' == modules.process_query('margarita cocktail')[0])
    assert ('cocktail' != modules.process_query('test')[0])
