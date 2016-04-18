from modules.src import movie

def test_movie():
    assert(movie.match('happyness movie') == True)
    assert(movie.match('happyness') == False)
    assert(movie.match('something random') == False)
