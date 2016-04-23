import modules

def test_weather():
    assert('weather' == modules.process_query('tell me the weather in city')[0])
    assert('weather' == modules.process_query('weather city')[0])
    assert('weather' == modules.process_query('whats the weather in city')[0])
    assert('weather' != modules.process_query('something random')[0])
