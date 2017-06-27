import modules


def test_weather():
    assert ('weather' == modules.process_query('tell me the weather in London')[0])
    assert ('weather' == modules.process_query('weather Delhi')[0])
    assert ('weather' == modules.process_query('What\'s the weather in Texas?')[0])
    assert ('weather' != modules.process_query('something random')[0])
