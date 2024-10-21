from camp import get_count_of_fully_overlapping_section_assignments, get_count_of_overlapping_section_assignments


def test_get_count_of_fully_overlapping_section_assignments():
    assert get_count_of_fully_overlapping_section_assignments('test_input.raw') == 2


def test_get_count_of_overlapping_section_assignments():
    assert get_count_of_overlapping_section_assignments('test_input.raw') == 4
