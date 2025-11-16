from cookie_lab import find_best_recipe


def test_find_best_recipe():
    assert find_best_recipe('test_input.raw') == 62842880
