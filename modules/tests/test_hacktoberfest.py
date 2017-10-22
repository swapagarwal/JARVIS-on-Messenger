import modules


def test_hacktoberfest():
    assert ('hacktoberfest' == modules.process_query('hacktoberfest')[0])
    assert ('news' == modules.process_query('acetheninja hacktoberfest')[0])
    assert ('news' == modules.process_query('hacktoberfest lokiiarora')[0])
    assert ('news' != modules.process_query('hack lol')[0])