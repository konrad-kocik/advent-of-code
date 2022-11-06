from seats_arranger import calculate_occupied_seats_for_close_neighbours, \
    calculate_occupied_seats_for_distant_neighbours


def test_calculate_occupied_seats_for_close_neighbours():
    assert calculate_occupied_seats_for_close_neighbours('test_input.raw') == 37


def test_calculate_occupied_seats_for_distant_neighbours():
    assert calculate_occupied_seats_for_distant_neighbours('test_input.raw') == 26
