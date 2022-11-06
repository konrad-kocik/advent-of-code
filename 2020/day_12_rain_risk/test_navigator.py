from navigator import calculate_manhattan_distance


def test_calculate_manhattan_distance():
    assert calculate_manhattan_distance('test_input.raw') == 25
