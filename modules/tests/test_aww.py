import modules


def test_weather():
    assert ('aww' == modules.process_query('aww')[0])
    assert ('aww' == modules.process_query('show me something cute')[0])
    assert ('aww' != modules.process_query('something random')[0])
