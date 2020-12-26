from searcher_part_1 import get_number_of_bags_which_contain


def test_get_number_of_bags_which_contain():
    result = get_number_of_bags_which_contain('shiny gold', 'test_input_part_1.raw')
    assert result == 4
