from lava_island_hiking_guide import calculate_sum_of_trailhead_scores


def test_calculate_sum_of_trailhead_scores():
    assert calculate_sum_of_trailhead_scores('test_input.raw') == 36
