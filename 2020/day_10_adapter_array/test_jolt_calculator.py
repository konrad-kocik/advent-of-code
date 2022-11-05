from jolt_calculator import calculate_jolt_differences


def test_calculate_jolt_differences():
    assert calculate_jolt_differences('test_input.raw') == {1: 22, 3: 10}
