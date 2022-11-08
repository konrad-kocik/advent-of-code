from computer import calculate_memory_sum


def test_calculate_memory_sum():
    assert calculate_memory_sum('test_input.raw') == 165
