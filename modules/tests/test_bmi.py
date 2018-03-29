import modules


def test_bmi():
    assert ('bmi' == modules.process_query('Am I ideal? 120 65')[0])
    assert ('bmi' == modules.process_query('What is my health situation? 110 75')[0])
    assert ('bmi' == modules.process_query('Do I need to loose weight? 130 100')[0])
    assert ('bmi' != modules.process_query('something random')[0])
