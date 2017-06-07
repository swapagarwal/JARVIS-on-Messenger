import modules

def test_time():
    assert('howto' == modules.process_query('how to crack knuckles')[0])
    assert('howto' == modules.process_query('how to pitch a tent')[0])
    assert('howto' == modules.process_query('how do I cut a watermelon')[0])
    assert('howto' != modules.process_query('something random')[0])
