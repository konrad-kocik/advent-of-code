from easter_bunny_headquarters import calculate_safety_factor, wait_for_easter_egg

print('\nSolving first part of puzzle')
safety_factor = calculate_safety_factor('input.raw', area_width=101, area_height=103)
print(f'Answer to first part of puzzle is: {safety_factor}')

print('\nSolving second part of puzzle')
seconds_elapsed = wait_for_easter_egg('input.raw', area_width=101, area_height=103)
print(f'Answer to second part of puzzle is: {seconds_elapsed}')
