import modules


def test_wallpaper():
    assert ('wallpaper' == modules.process_query('wallpaper')[0])
    assert ('wallpaper' == modules.process_query('i need a new wallpaper')[0])
    assert ('wallpaper' == modules.process_query('show me a random wallpaper')[0])
    assert ('wallpaper' == modules.process_query('random wallpaper')[0])
    assert ('wallpaper' != modules.process_query('latest news')[0])
