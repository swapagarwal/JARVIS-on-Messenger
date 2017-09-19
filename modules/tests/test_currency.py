import modules


def test_currency():
    assert ('currency' == modules.process_query('HKD to USD')[0])
    assert ('currency' == modules.process_query('USD to INR')[0])
    assert ('currency' == modules.process_query('how much is USD in EUR')[0])

    intent, entities = modules.process_query('convert 5 HKD to USD')
    assert ('currency' == intent)
    assert ('HKD' == entities['from_currency'][0]['value'])
    assert ('USD' == entities['to_currency'][0]['value'])
    assert (5 == entities['number'][0]['value'])

    intent, entities = modules.process_query('how much is 100 USD to INR')
    assert ('currency' == intent)
    assert ('USD' == entities['from_currency'][0]['value'])
    assert ('INR' == entities['to_currency'][0]['value'])
    assert (100 == entities['number'][0]['value'])

    assert ('currency' != modules.process_query('something random')[0])
