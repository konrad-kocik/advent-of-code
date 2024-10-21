from giant_cargo_crane import move_crates, move_crates_with_cm9001


def test_move_crates():
    assert move_crates('test_input.raw') == 'CMZ'


def test_move_crates_with_cm9001():
    assert move_crates_with_cm9001('test_input.raw') == 'MCD'
