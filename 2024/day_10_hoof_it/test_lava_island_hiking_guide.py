from lava_island_hiking_guide import rate_trailheads


def test_rate_trailheads():
    assert rate_trailheads('test_input.raw') == 36


def test_rate_trailheads_with_distinct_trails():
    assert rate_trailheads('test_input.raw', distinct_trails=True) == 81
