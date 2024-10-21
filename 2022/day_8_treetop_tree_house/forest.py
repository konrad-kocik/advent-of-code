def count_visible_trees(file_path):
    forest = _get_forest(file_path)
    trees_visibility = _mark_visible_trees(forest)
    visible_trees_count = _count_visible_trees(trees_visibility)
    return visible_trees_count


def find_tree_with_highest_scenic_score(file_path):
    forest = _get_forest(file_path)
    trees_scenic_scores = _rate_trees_scenic_score(forest)
    highest_scenic_score = _find_highest_scenic_score(trees_scenic_scores)
    return highest_scenic_score


def _get_forest(file_path):
    forest = []

    with open(file_path, 'r') as file:
        for line in file:
            forest.append([int(tree) for tree in line.strip()])

    return forest


def _mark_visible_trees(forest):
    forest_visibility = []

    for row_id, row in enumerate(forest):
        row_visibility = []

        for tree_id, tree in enumerate(row):
            tree_visibility = any([_is_tree_visible_from_north(forest, row_id, tree_id),
                                   _is_tree_visible_from_south(forest, row_id, tree_id),
                                   _is_tree_visible_from_east(forest, row_id, tree_id),
                                   _is_tree_visible_from_west(forest, row_id, tree_id)])
            row_visibility.append(tree_visibility)

        forest_visibility.append(row_visibility)

    return forest_visibility


def _is_tree_visible_from_north(forest, row_id_to_check, tree_id_to_check):
    for curr_row_id, curr_row in enumerate(forest):
        if curr_row_id < row_id_to_check:
            if curr_row[tree_id_to_check] >= forest[row_id_to_check][tree_id_to_check]:
                return False
    return True


def _is_tree_visible_from_south(forest, row_id_to_check, tree_id_to_check):
    for curr_row_id, curr_row in enumerate(forest):
        if curr_row_id > row_id_to_check:
            if curr_row[tree_id_to_check] >= forest[row_id_to_check][tree_id_to_check]:
                return False
    return True


def _is_tree_visible_from_east(forest, row_id_to_check, tree_id_to_check):
    for curr_tree_id, curr_tree in enumerate(forest[row_id_to_check]):
        if curr_tree_id > tree_id_to_check:
            if curr_tree >= forest[row_id_to_check][tree_id_to_check]:
                return False
    return True


def _is_tree_visible_from_west(forest, row_id_to_check, tree_id_to_check):
    for curr_tree_id, curr_tree in enumerate(forest[row_id_to_check]):
        if curr_tree_id < tree_id_to_check:
            if curr_tree >= forest[row_id_to_check][tree_id_to_check]:
                return False
    return True


def _count_visible_trees(trees_visibility):
    visible_trees_count = 0

    for row in trees_visibility:
        for visibility in row:
            visible_trees_count += 1 if visibility else 0

    return visible_trees_count


def _rate_trees_scenic_score(forest):
    forest_scenic_scores = []

    for row_id, row in enumerate(forest):
        row_scenic_scores = []

        for tree_id, tree in enumerate(row):
            tree_scenic_score = _rate_tree_scenic_score_due_north(forest, row_id, tree_id) * \
                                _rate_tree_scenic_score_due_south(forest, row_id, tree_id) * \
                                _rate_tree_scenic_score_due_east(forest, row_id, tree_id) * \
                                _rate_tree_scenic_score_due_west(forest, row_id, tree_id)
            row_scenic_scores.append(tree_scenic_score)

        forest_scenic_scores.append(row_scenic_scores)

    return forest_scenic_scores


def _rate_tree_scenic_score_due_north(forest, row_id, tree_id):
    tree_scenic_score = 0
    clear_view = True
    row_id_to_check = row_id - 1

    while clear_view and row_id_to_check >= 0:
        tree_scenic_score += 1

        if forest[row_id_to_check][tree_id] < forest[row_id][tree_id]:
            row_id_to_check -= 1
        else:
            clear_view = False

    return tree_scenic_score


def _rate_tree_scenic_score_due_south(forest, row_id, tree_id):
    tree_scenic_score = 0
    clear_view = True
    row_id_to_check = row_id + 1

    while clear_view and row_id_to_check < len(forest):
        tree_scenic_score += 1

        if forest[row_id_to_check][tree_id] < forest[row_id][tree_id]:
            row_id_to_check += 1
        else:
            clear_view = False

    return tree_scenic_score


def _rate_tree_scenic_score_due_east(forest, row_id, tree_id):
    tree_scenic_score = 0
    clear_view = True
    row_to_check = forest[row_id]
    tree_id_to_check = tree_id + 1

    while clear_view and tree_id_to_check < len(row_to_check):
        tree_scenic_score += 1

        if row_to_check[tree_id_to_check] < forest[row_id][tree_id]:
            tree_id_to_check += 1
        else:
            clear_view = False

    return tree_scenic_score


def _rate_tree_scenic_score_due_west(forest, row_id, tree_id):
    tree_scenic_score = 0
    clear_view = True
    row_to_check = forest[row_id]
    tree_id_to_check = tree_id - 1

    while clear_view and tree_id_to_check >= 0:
        tree_scenic_score += 1
        if row_to_check[tree_id_to_check] < forest[row_id][tree_id]:
            tree_id_to_check -= 1
        else:
            clear_view = False

    return tree_scenic_score


def _find_highest_scenic_score(scenic_scores):
    highest_scenic_score = 0

    for row in scenic_scores:
        for score in row:
            highest_scenic_score = score if score > highest_scenic_score else highest_scenic_score

    return highest_scenic_score
