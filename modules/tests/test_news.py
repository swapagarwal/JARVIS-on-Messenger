import modules

def test_news():
	assert('news' == modules.process_query("what's the latest on the facebook case")[0])
	assert('news' == modules.process_query("What's happening around the world")[0])
	assert('news' == modules.process_query("What's the latest on fashion news")[0])
	assert('news' != modules.process_query("something random")[0])