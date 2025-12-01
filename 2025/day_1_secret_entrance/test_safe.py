from safe import Safe


def test_input_combination():
    safe = Safe()
    safe.input_combination('test_input.raw')
    assert safe.zeroes_count == 3


def test_input_combination_with_intermediate_zeroes_counting():
    safe = Safe()
    safe.input_combination('test_input.raw', count_intermediate_zeroes=True)
    assert safe.zeroes_count == 6
