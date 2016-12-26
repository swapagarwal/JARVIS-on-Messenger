import modules

def test_math():
    assert('math' == modules.process_query('Can you solve 2 + 2')[0])
    assert('math' == modules.process_query('Can you evaluate 2 + 2')[0])
