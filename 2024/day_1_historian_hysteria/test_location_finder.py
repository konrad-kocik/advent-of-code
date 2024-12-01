from location_finder import calculate_total_distance_between_lists, calculate_similarity_score


def test_calculate_total_distance_between_lists():
    assert calculate_total_distance_between_lists('test_input.raw') == 11


def test_calculate_similarity_score():
    assert calculate_similarity_score('test_input.raw') == 31
