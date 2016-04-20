from modules.src import dictionary

def test_joke():
    assert(dictionary.match('jarvis definition') == True)
    assert(dictionary.match('word definition') == True)
    assert(dictionary.match('computer definition') == True)
    assert(dictionary.match('definition definition') == True)
    assert(dictionary.match('jarvis jarvis') == False)
    assert(dictionary.match('something random') == False)
