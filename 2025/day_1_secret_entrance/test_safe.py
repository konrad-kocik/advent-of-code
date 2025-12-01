from safe import Safe


def test_zeroes_count():
    safe = Safe()
    safe.input_combination('test_input.raw')
    assert safe.zeroes_count == 3
