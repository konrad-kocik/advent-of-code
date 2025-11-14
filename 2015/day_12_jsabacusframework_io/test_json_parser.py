from json_parser import sum_all_numbers


def test_sum_all_numbers():
    assert sum_all_numbers('test_input.json') == 18
