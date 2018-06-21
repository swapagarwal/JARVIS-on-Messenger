import modules


def test_football():
    assert ('football' == modules.process_query('football league in england')[0])
    assert ('football' == modules.process_query('football league in italy')[0])
    assert ('football' == modules.process_query('football league in france')[0])
    assert ('football' != modules.process_query('Who won the football league in germany?')[0])
