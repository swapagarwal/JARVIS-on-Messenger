from modules.src import hello

def test_joke():
    assert(hello.match('Are you there?') == True)
    assert(hello.match('Hi, Jarvis!') == True)
    assert(hello.match('hello') == True)
    assert(hello.match('jarvis jarvis') == False)
    assert(hello.match('something random') == False)
