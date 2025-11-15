from race import race


def test_race():
    winner, result = race('test_input.raw', duration=1000)
    assert winner == 'Comet'
    assert result == 1120


def test_race_with_new_scoring_system():
    winner, result = race('test_input.raw', duration=1000, new_scoring_system=True)
    assert winner == 'Dancer'
    assert result == 689
