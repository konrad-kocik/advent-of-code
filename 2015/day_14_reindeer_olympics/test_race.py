from race import race


def test_race():
    winner, distance = race('test_input.raw', duration=1000)
    assert winner == 'Comet'
    assert distance == 1120
