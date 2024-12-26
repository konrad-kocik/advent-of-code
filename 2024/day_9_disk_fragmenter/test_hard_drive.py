from hard_drive import calculate_filesystem_checksum


def test_calculate_filesystem_checksum():
    assert calculate_filesystem_checksum('test_input.raw') == 1928


def test_calculate_filesystem_checksum_with_moving_whole_files():
    assert calculate_filesystem_checksum('test_input.raw', move_whole_files=True) == 2858
