from navigator import calculate_manhattan_distance, calculate_manhattan_distance_with_waypoint


def test_calculate_manhattan_distance():
    assert calculate_manhattan_distance('test_input.raw') == 25


def test_calculate_manhattan_distance_with_waypoint():
    assert calculate_manhattan_distance_with_waypoint('test_input.raw') == 286
