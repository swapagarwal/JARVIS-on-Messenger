import modules


def test_bmi():
    assert ('bmi' == modules.process_query('bmi Am I ideal? 120 65 imperial')[0])
    assert ('bmi' == modules.process_query('bmi What is my health situation? 110 75 imperial')[0])
    assert ('bmi' == modules.process_query('bmi Do I need to loose weight? 165 70 metric')[0])
    assert ('bmi' != modules.process_query('something random')[0])
