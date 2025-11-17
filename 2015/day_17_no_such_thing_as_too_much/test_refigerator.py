from refrigerator import count_possible_containers_combinations


def test_count_possible_containers_combinations():
    assert count_possible_containers_combinations('test_input.raw', eggnog_amount=25) == 4
