import modules

def test_angry():
    assert('angry' == modules.process.query('angry')[0])
    assert('angry' == modules.process.query('i am angry')[0])
    assert('angry' == modules.process.query('i can not control my anger.')[0])
    assert('angry' != modules.process.query('happy')[0])
