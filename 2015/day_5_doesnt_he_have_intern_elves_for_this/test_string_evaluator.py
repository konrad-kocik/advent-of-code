from string_evaluator import count_nice_strings


def test_count_nice_strings():
    assert count_nice_strings('test_input_1.raw') == 2


def test_count_nice_strings_with_new_rules():
    assert count_nice_strings('test_input_2.raw', new_rules=True) == 2
