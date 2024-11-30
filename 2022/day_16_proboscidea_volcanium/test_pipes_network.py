from pipes_network import find_maximum_pressure_release


def test_find_maximum_pressure_release():
    assert find_maximum_pressure_release('test_input.raw') == 1651
