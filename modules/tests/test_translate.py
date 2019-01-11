import modules

def test_translate():
    assert ('translate' == modules.process_query('translate hi, my name is Foo to spanish')[0])
    assert ('translate' == modules.process_query('translate where is the nearest restaurant? to german')[0])
    assert ('translate' == modules.process_query('translate i am eating from english to french')[0])
    assert ('translate' != modules.process_query('something random')[0])
