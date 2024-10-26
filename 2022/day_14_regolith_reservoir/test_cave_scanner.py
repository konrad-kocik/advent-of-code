from cave_scanner import count_units_of_resting_sand_after_simulation


def test_count_units_of_resting_sand():
    assert count_units_of_resting_sand_after_simulation('test_input.raw') == 24


def test_count_units_of_resting_sand_with_cave_floor():
    assert count_units_of_resting_sand_after_simulation('test_input.raw', include_floor=True) == 93
