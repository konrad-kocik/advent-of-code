from physics_defying_stones import count_stones


def test_count_stones():
    assert count_stones('test_input.raw', blinks_count=6) == 22
