from forest import count_visible_trees, find_tree_with_highest_scenic_score

print('\nSolving first part of puzzle')
visible_trees_count = count_visible_trees('input.raw')
print(f'Answer to first part of puzzle is: {visible_trees_count}')

print('\nSolving second part of puzzle')
highest_scenic_score = find_tree_with_highest_scenic_score('input.raw')
print(f'Answer to second part of puzzle is: {highest_scenic_score}')
