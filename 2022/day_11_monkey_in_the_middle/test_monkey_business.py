from monkey_business import calculate_level_of_monkey_business


def test_calculate_level_of_monkey_business():
    assert calculate_level_of_monkey_business('test_input.raw', rounds=20) == 10605


def test_calculate_level_of_monkey_business_with_no_worry_decrease():
    assert calculate_level_of_monkey_business('test_input.raw', rounds=10000, worry_decrease=False) == 2713310158
