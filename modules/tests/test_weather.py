import modules

def test_weather():
    assert('weather' == modules.process_query('tell me the weather in London')[0])
    assert('weather' == modules.process_query('weather London')[0])
    assert('weather' == modules.process_query('whats the weather in London')[0])
    assert('weather' != modules.process_query('something random')[0])
