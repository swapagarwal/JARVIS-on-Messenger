import modules

def test_synonym():
    assert ('synonym' == modules.process_query('synonym sad')[0])
    assert ('synonym' == modules.process_query('happy synonym')[0])
    assert ('synonym' == modules.process_query('synonymous with run?')[0])
    assert ('synonym' != modules.process_query('random message')[0])