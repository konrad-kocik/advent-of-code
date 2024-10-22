from reactor import boot


def test_boot():
    assert boot('test_input.raw', cycles=6) == 112
