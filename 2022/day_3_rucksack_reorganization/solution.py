from inventory import get_sum_of_duplicated_item_type_priorities, get_sum_of_badge_priorities

print('\nSolving first part of puzzle')
sum_of_duplicated_item_type_priorities = get_sum_of_duplicated_item_type_priorities('input.raw')
print(f'Answer to first part of puzzle is: {sum_of_duplicated_item_type_priorities}')

print('\nSolving second part of puzzle')
sum_of_badge_priorities = get_sum_of_badge_priorities('input.raw')
print(f'Answer to second part of puzzle is: {sum_of_badge_priorities}')
