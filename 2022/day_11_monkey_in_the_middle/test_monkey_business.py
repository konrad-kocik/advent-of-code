from monkey_business import calculate_level_of_monkey_business


def test_calculate_level_of_monkey_business():
    assert calculate_level_of_monkey_business('test_input.raw', rounds=20) == 10605
