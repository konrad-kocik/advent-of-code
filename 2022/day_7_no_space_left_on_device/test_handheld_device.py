from handheld_device import get_total_size_of_small_dirs, get_total_size_of_smallest_dir_to_delete


def test_get_total_size_of_small_dirs():
    assert get_total_size_of_small_dirs('test_input.raw') == 95437


def test_get_total_size_of_smallest_dir_to_delete():
    assert get_total_size_of_smallest_dir_to_delete('test_input.raw') == 24933642
