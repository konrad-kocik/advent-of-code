from digital_list import calculate_code_representation_overhead, calculate_encoded_representation_overhead


def test_calculate_code_representation_overhead():
    assert calculate_code_representation_overhead('test_input.raw') == 12


def test_calculate_encoded_representation_overhead():
    assert calculate_encoded_representation_overhead('test_input.raw') == 19
