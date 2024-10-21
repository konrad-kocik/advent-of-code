from forest import count_visible_trees, find_tree_with_highest_scenic_score


def test_count_visible_trees():
    assert count_visible_trees('test_input.raw') == 21


def test_find_tree_with_highest_scenic_score():
    assert find_tree_with_highest_scenic_score('test_input.raw') == 8
