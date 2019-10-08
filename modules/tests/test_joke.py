import modules
import config
import json


def test_joke():
    assert ('joke' == modules.process_query('tell me a joke')[0])
    assert ('joke' == modules.process_query('Do you know a joke?')[0])
    assert ('joke' == modules.process_query('random jokes')[0])
    assert ('joke' != modules.process_query('something random')[0])
    with open(config.JOKES_SOURCE_FILE) as jokes_file:
        jokes = json.load(jokes_file)
        assert len(jokes['jokes']) == len(set(jokes['jokes']))
