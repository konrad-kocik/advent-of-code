from inventory import get_sum_of_duplicated_item_type_priorities, get_sum_of_badge_priorities


def test_get_sum_of_duplicated_item_type_priorities():
    assert get_sum_of_duplicated_item_type_priorities('test_input.raw') == 157


def test_get_sum_of_badge_priorities():
    assert get_sum_of_badge_priorities('test_input.raw') == 70
