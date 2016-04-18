from modules.src import joke

def test_joke():
    assert(joke.match('tell me a joke') == True)
    assert(joke.match('random jokes') == True)
    assert(joke.match('Do you know a joke?') == True)
    assert(joke.match('joke is the') == False)
    assert(joke.match('something random') == False)
