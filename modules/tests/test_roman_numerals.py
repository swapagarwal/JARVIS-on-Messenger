import modules


def test_roman_numerals():
    assert ('roman_numerals' == modules.process_query('write 400 as roman numrals')[0])
    assert ('roman_numerals' == modules.process_query('write 768 in roman number')[0])
    assert ('roman_numerals' == modules.process_query('how do you write 56 in roman numrals')[0])
    assert ('roman_numerals' != modules.process_query('what is a duck')[0])
