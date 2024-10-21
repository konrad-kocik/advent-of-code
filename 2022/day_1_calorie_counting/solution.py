from backpack import find_max_calories, get_top_three_calories_sum

print('\nSolving first part of puzzle')
max_calories = find_max_calories('input.raw')
print(f'Answer to first part of puzzle is: {max_calories}')

print('\nSolving second part of puzzle')
top_three_calories_sum = get_top_three_calories_sum('input.raw')
print(f'Answer to second part of puzzle is: {top_three_calories_sum}')
