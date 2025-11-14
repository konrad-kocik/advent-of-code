from dinner_table import find_best_arrangement

print('Solving first part of puzzle')
best_arrangement_rating = find_best_arrangement('input.raw')
print(f'Answer to first part of puzzle is: {best_arrangement_rating}')

print('Solving second part of puzzle')
best_arrangement_rating = find_best_arrangement('input.raw', include_host=True)
print(f'Answer to second part of puzzle is: {best_arrangement_rating}')
