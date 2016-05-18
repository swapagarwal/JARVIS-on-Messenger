import modules

def test_news():
	assert('news' == modules.process_query("United States Election")[0])
	assert('news' == modules.process_query("What's happening around the world")[0])
	assert('news' == modules.process_query("What's the latest on fashion news")[0])
	assert('news' == modules.process_query("something random")[0])