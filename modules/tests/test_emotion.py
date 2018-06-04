import modules
def test_hello():
  assert('emotion'==modules.process_query('i love you')[0])
  assert('emotion'==modules.process_query('i like you')[0])
  assert('emotion'==modules.process_query('i missed you')[0])
  assert('emotion'==modules.process_query('what is love')[0]) 
