from seats_arranger import calculate_occupied_seats


def test_calculate_occupied_seats():
    assert calculate_occupied_seats('test_input.raw') == 37
