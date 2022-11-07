from bus_scheduler import calculate_earliest_bus


def test_calculate_earliest_bus():
    assert calculate_earliest_bus('test_input.raw') == 295
