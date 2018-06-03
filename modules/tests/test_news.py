import modules

def test_news():
	assert('news' == modules.process_query('What todays news in Australia?')[0])
	assert('news' == modules.process_query('Whats the news headline?')[0])
	assert('news' == modules.process_query('headline, please')[0])
	assert('news' != modules.process_query('something random')[0])

