from bus_scheduler import calculate_earliest_bus_hash, find_sequential_bus_departure_timestamp


def test_calculate_earliest_bus():
    assert calculate_earliest_bus_hash('test_input.raw') == 295


def test_find_sequential_bus_departure_timestampt():
    assert find_sequential_bus_departure_timestamp('test_input.raw') == 1068781
