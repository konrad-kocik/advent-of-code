from cave_scanner import count_units_of_resting_sand_after_simulation

print('\nSolving first part of puzzle')
resting_sand_count = count_units_of_resting_sand_after_simulation('input.raw')
print(f'Answer to first part of puzzle is: {resting_sand_count}')

print('\nSolving second part of puzzle')
resting_sand_count = count_units_of_resting_sand_after_simulation('input.raw', include_floor=True)
print(f'Answer to second part of puzzle is: {resting_sand_count}')
