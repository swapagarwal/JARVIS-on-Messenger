import modules


def test_dictionary():
    assert ('roman_numerals' == modules.process_query('write 400 as roman numrals')[0])
    assert ('roman_numerals' == modules.process_query('write 768 in roman number')[0])
    assert ('roman_numerals' == modules.process_query('how do you write 56 in roman numrals')[0])
    assert ('roman_numerals' != modules.process_query('can you tell med what 587 is in roman numbers')[0])
