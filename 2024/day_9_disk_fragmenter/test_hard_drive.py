from hard_drive import calculate_filesystem_checksum


def test_calculate_filesystem_checksum():
    assert calculate_filesystem_checksum('test_input.raw') == 1928
