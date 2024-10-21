from giant_cargo_crane import move_crates, move_crates_with_cm9001

print('\nSolving first part of puzzle')
top_crates = move_crates('input.raw')
print(f'Answer to first part of puzzle is: {top_crates}')

print('\nSolving second part of puzzle')
top_crates = move_crates_with_cm9001('input.raw')
print(f'Answer to second part of puzzle is: {top_crates}')
