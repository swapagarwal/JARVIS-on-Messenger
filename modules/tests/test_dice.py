import modules


def test_dice():
    assert ('dice' == modules.process_query('Roll a dice')[0])
    assert ('dice' == modules.process_query('Roll a die')[0])
    assert ('dice' == modules.process_query('Jarvis, roll a dice')[0])
    assert ('dice' == modules.process_query('Jarvis, roll a die')[0])
    assert ('dice' == modules.process_query('Jarvis, roll a d4')[0])
    assert ('dice' == modules.process_query('Can you roll a dice?')[0])
    assert ('dice' == modules.process_query('Roll a d6')[0])
    assert ('dice' == modules.process_query('Roll a D6')[0])
    assert ('dice' == modules.process_query('Roll a D20')[0])
    assert ('dice' != modules.process_query('something random')[0])
