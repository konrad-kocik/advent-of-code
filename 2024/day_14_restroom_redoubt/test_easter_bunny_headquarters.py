from easter_bunny_headquarters import calculate_safety_factor


def test_calculate_safety_factor():
    assert calculate_safety_factor('test_input.raw', area_width=11, area_height=7) == 12
