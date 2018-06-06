import modules

def test_calculator():
    assert('calculator' == modules.process_query('Can you evaluate 3 + 4')[0])
    assert('calculator' == modules.process_query('Can you solve 3 + 4')[0])
    assert('calculator' == modules.process_query('What is 3 + 4')[0])
