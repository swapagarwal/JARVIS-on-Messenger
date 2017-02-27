import modules
import pytest

def test_twitter():
    assert('twitter' == modules.process_query('twitter')[0])
    assert('twitter' == modules.process_query('twitter hotnews')[0])
    assert('twitter' == modules.process_query('paris twitter')[0])
    assert('twitter' != modules.process_query('something random')[0])

    intent, entities = modules.process_query('twitter @NBA')
    assert('twitter' == intent)
    assert('@nba' == entities['twitter'][0]['value'].lower())


    intent, entities = modules.process_query('twitter')
    assert('twitter' == intent)
    with pytest.raises(KeyError):
      assert(entities['twitter'][0]['value'].lower())
    

    intent, entities = modules.process_query('twitter @POTUS')
    assert('twitter' == intent)
    assert('@potus' == entities['twitter'][0]['value'].lower())

    intent, entities = modules.process_query('twitter someone')
    assert('twitter' == intent)
    assert('someone' == entities['twitter'][0]['value'].lower())

    intent, entities = modules.process_query('twitter zidane')
    assert('twitter' == intent)
    assert('zidane' == entities['twitter'][0]['value'].lower())
