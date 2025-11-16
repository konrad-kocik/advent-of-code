from cookie_lab import find_best_recipe


def test_find_best_recipe():
    assert find_best_recipe('test_input.raw') == 62842880


def test_find_best_recipe_with_calories_requirement():
    assert find_best_recipe('test_input.raw', calories_requirement=500) == 57600000
