import modules

def test_foodmenu():
    assert ('menu' == modules.process_query('give me a menu')[0])
    assert ('menu' == modules.process_query('What should I eat?')[0])
    assert ('menu' == modules.process_query('Choose a menu')[0])
    assert ('menu' == modules.process_query('Pick me a menu')[0])
    assert ('menu' != modules.process_query('something random')[0])
