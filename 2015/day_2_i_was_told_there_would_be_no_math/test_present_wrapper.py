from wrapping_station import calculate_wrapping_paper_order, calculate_ribbon_order


def test_calculate_wrapping_paper_order():
    assert calculate_wrapping_paper_order('test_input.raw') == 101


def test_calculate_ribbon_order():
    assert calculate_ribbon_order('test_input.raw') == 48
