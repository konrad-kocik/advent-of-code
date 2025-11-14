from json_parser import sum_all_numbers


def test_sum_all_numbers():
    assert sum_all_numbers('test_input_1.json') == 18


def test_sum_all_numbers_with_ignored_property():
    assert sum_all_numbers('test_input_2.json', ignored_property='red') == 16
