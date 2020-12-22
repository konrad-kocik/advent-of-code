from handy_haversacks import get_number_of_bags_which_contain


def test_get_number_of_bags_which_contain():
    result = get_number_of_bags_which_contain('shiny gold', 'test_input.raw')
    assert result == 4
