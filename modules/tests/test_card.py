import modules

def test_card():
    assert ('card' == modules.process_query('draw a card')[0])
    assert ('card' == modules.process_query('Can you draw a playing card?')[0])
    assert ('card' == modules.process_query('show me a playing card')[0])
    assert ('card' != modules.process_query('something random')[0])