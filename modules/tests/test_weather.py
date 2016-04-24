import modules

def test_weather():
    assert('weather' == modules.process_query('tell me the weather in london')[0])
    assert('weather' == modules.process_query('weather london')[0])
    assert('weather' == modules.process_query('whats the weather in london')[0])
    assert('weather' != modules.process_query('something random')[0])
