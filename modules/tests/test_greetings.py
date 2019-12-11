import modules


def test_greetings():
    assert ('greetings' == modules.process_query('is today a holiday')[0])
    assert ('greetings' == modules.process_query('what is today')[0])
