import modules

def test_password():
    assert('password' == modules.process_query('5 digit password')[0])
    assert('password' == modules.process_query('passphrase')[0])
    assert('password' == modules.process_query('strong pw')[0])
    assert('password' == modules.process_query('pwgen 7')[0])
    assert('password' == modules.process_query('random password')[0])
    assert('password' != modules.process_query('something different')[0])
