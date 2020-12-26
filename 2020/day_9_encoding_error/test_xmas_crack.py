from xmas_crack import find_weakness


def test_find_weakness():
    assert find_weakness('test_input.raw', preamble_size=5) == 62
