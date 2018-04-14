import modules


def test_manga():
    assert ('manga' == modules.process_query('Naruto manga')[0])
    assert ('manga' == modules.process_query('One Piece manga status')[0])
    assert ('manga' == modules.process_query('Information on Bleach manga')[0])
    assert ('manga' != modules.process_query('something random')[0])