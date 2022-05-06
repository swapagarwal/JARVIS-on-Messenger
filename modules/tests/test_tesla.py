import modules


def test_video():
    assert ('tesla' == modules.process_query('tesla stock')[0])
    assert ('tesla' == modules.process_query('tesla cars')[0])
    assert ('tesla' == modules.process_query('tesla elon musk')[0])
    assert ('tesla' != modules.process_query('something random')[0])
