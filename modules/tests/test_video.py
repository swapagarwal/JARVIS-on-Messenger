import modules


def test_video():
    assert ('video' == modules.process_query('sia videos')[0])
    assert ('video' == modules.process_query('videos by eminem')[0])
    assert ('video' == modules.process_query('video coldplay')[0])
    assert ('video' != modules.process_query('something random')[0])
    assert ('video' == modules.process_query('trending videos US')[0])
    assert ('video' == modules.process_query('trending videos from MX')[0])
    assert ('video' != modules.process_query('trending in Europe')[0])
