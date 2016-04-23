import modules

def test_wiki():
    assert('wiki' == modules.process_query('Wikipedia Barack')[0])
    assert('wiki' == modules.process_query('Wikipedia HTML')[0])
    assert('wiki' != modules.process_query('joke definition')[0])
