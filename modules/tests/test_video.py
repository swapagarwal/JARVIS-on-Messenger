import modules


def test_video():
    assert ('video' == modules.process_query('sia videos')[0])
    assert ('video' == modules.process_query('videos by eminem')[0])
    assert ('video' == modules.process_query('video coldplay')[0])
    assert ('video' != modules.process_query('something random')[0])
