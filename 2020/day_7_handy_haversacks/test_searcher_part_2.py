from searcher_part_2 import get_number_of_bags_contained_in


def test_get_number_of_bags_contained_in():
    result = get_number_of_bags_contained_in('shiny gold', 'test_input_part_2.raw')
    assert result == 126
