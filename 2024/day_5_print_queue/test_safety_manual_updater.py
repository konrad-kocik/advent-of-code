from safety_manual_updater import add_up_middle_page_numbers_from_correct_updates


def test_add_up_middle_page_numbers_from_correct_updates():
    assert add_up_middle_page_numbers_from_correct_updates('test_input.raw') == 143
