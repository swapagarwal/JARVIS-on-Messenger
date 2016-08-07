import modules

def test_coinflip():
        assert('coin' == modules.process_query('Flip a coin')[0])
        assert('coin' == modules.process_query('Jarvis flip a coin')[0])
        assert('coin' == modules.process_query('Can you flip a coin')[0])
        assert('coin' != modules.process_query('something random')[0])
