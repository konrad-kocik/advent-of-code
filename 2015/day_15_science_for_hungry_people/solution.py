from cookie_lab import find_best_recipe

print('Solving first part of puzzle')
best_recipe_score = find_best_recipe('input.raw')
print(f'Answer to first part of puzzle is: {best_recipe_score}')

print('Solving second part of puzzle')
best_recipe_score = find_best_recipe('input.raw', calories_requirement=500)
print(f'Answer to second part of puzzle is: {best_recipe_score}')
