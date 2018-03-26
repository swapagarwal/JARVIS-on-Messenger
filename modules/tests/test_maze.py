import modules


def test_maze():
    assert ('maze' == modules.process_query('Maze of size 10')[0])
    assert ('maze' == modules.process_query('Show me a maze of size 10')[0])
    assert ('maze' == modules.process_query('Give me a maze 10 big')[0])
