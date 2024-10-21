from backpack import find_max_calories, get_top_three_calories_sum


def test_find_max_calories():
    assert find_max_calories('test_input.raw') == 24000


def test_get_top_three_calories_sum():
    assert get_top_three_calories_sum('test_input.raw') == 45000
