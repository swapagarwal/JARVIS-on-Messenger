import modules


def test_crypto():
    assert ('crypto' == modules.process_query('BTC to LTC')[0])
    assert ('crypto' == modules.process_query('NAV to BTC')[0])
    assert ('crypto' == modules.process_query('BTC-ETH')[0])

    intent, entities = modules.process_query('cryptocurrency BTC-ETH')
    assert ('crypto' == intent)
    assert ('BTC-ETH' == entities['market'][0]['value'])

    intent, entities = modules.process_query('ticker info for ETH to OMG')
    assert ('crypto' == intent)
    assert ('ETH to OMG' == entities['market'][0]['value'])

    intent, entities = modules.process_query('market ETH to OMG')
    assert ('crypto' == intent)
    assert ('ETH to OMG' == entities['market'][0]['value'])

    intent, entities = modules.process_query('crypto ETH to OMG')
    assert ('crypto' == intent)
    assert ('ETH to OMG' == entities['market'][0]['value'])

    assert ('crypto' != modules.process_query('tests invalid input')[0])
    