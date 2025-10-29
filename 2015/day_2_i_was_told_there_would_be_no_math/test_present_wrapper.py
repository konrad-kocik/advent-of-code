from wrapping_station import calculate_wrapping_paper_order


def test_calculate_wrapping_paper_order():
    assert calculate_wrapping_paper_order('test_input.raw') == 101
