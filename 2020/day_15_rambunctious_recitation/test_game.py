from pytest import mark

from game import play


@mark.parametrize('starting_numbers, game_result', [
    ([0, 3, 6], 436),
    ([1, 3, 2], 1),
    ([2, 1, 3], 10),
    ([1, 2, 3], 27),
    ([2, 3, 1], 78),
    ([3, 2, 1], 438),
    ([3, 1, 2], 1836)
])
def test_play(starting_numbers, game_result):
    assert play(final_turn=2020, numbers=starting_numbers) == game_result
