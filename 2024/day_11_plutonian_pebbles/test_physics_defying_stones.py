from pytest import mark

from physics_defying_stones import count_stones


@mark.parametrize('blinks_count, stones_count', [(6, 22),
                                                 (25, 55312)])
def test_count_stones(blinks_count, stones_count):
    assert count_stones('test_input.raw', blinks_count=blinks_count) == stones_count
