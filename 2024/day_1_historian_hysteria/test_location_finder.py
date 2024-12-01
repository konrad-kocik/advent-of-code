from location_finder import calculate_total_distance_between_lists


def test_calculate_total_distance_between_lists():
    assert calculate_total_distance_between_lists('test_input.raw') == 11
