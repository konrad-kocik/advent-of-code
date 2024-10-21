from cpu import calculate_sum_of_signal_strengths


def test_calculate_sum_of_signal_strengths():
    cycles = [20, 60, 100, 140, 180, 220]
    assert calculate_sum_of_signal_strengths('test_input.raw', cycles) == 13140
