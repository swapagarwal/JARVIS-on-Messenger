import modules


def test_menu():
    assert ('menu' == modules.process_query('give me a menu')[0])
    assert ('menu' == modules.process_query('i don\'t know what to eat')[0])
    assert ('menu' == modules.process_query('pick a menu')[0])
    assert ('menu' != modules.process_query('something random')[0])
