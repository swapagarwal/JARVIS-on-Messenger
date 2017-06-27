import modules


def test_dice():
    assert ('dice' == modules.process_query('Roll a dice')[0])
    assert ('dice' == modules.process_query('Jarvis, roll a dice')[0])
    assert ('dice' == modules.process_query('Can you roll a dice?')[0])
    assert ('dice' != modules.process_query('something random')[0])
