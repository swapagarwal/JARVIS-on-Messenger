import modules

def test_coinflip():
        assert('coinflip' == modules.process_query('Flip a coin'))[0]
        assert('coinflip' == modules.process_query('Jarvis flip a coin'))[0]
        assert('coinflip' == modules.process_query('Can you flip a coin'))[0]
        assert('coinflip' == modules.process_query('something random'))[0]
