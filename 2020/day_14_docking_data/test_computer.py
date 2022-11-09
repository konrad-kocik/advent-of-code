from computer import calculate_sum_of_memory, calculate_sum_of_memory_with_floating_addresses


def test_calculate_sum_of_memory():
    assert calculate_sum_of_memory('test_input.raw') == 165


def test_calculate_sum_of_memory_with_floating_addresses():
    assert calculate_sum_of_memory_with_floating_addresses('test_input_floating_addresses.raw') == 208
