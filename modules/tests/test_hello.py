import modules


def test_hello():
    assert ('hello' == modules.process_query('hello')[0])
    assert ('hello' == modules.process_query('Hi, Jarvis!')[0])
    assert ('hello' == modules.process_query('Are you there?')[0])
    assert ('hello' != modules.process_query('something random')[0])
