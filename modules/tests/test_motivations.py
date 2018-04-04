import modules


def test_motivation():
    assert ('motivation' == modules.process_query('tell me something motivational')[0])
    assert ('motivation' == modules.process_query('I need some encouragement')[0])
    assert ('motivation' == modules.process_query('random motivational quote')[0])
    assert ('motivation' != modules.process_query('motivational quote for today')[0])
