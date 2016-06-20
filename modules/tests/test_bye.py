import modules

def test_bye():
    assert('bye' == modules.process_query('bye')[0])
    assert('bye' == modules.process_query('byebye')[0])
    assert('bye' != modules.process_query('good time')[0])