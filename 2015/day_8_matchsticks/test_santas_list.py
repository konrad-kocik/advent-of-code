from digital_list import calculate_code_representation_overhead


def test_digital_list():
    assert calculate_code_representation_overhead('test_input.raw') == 12
