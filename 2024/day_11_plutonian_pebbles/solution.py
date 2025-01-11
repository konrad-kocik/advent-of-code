from physics_defying_stones import count_stones

print('\nSolving first part of puzzle')
stones_count = count_stones('input.raw', blinks_count=25)
print(f'Answer to first part of puzzle is: {stones_count}')

print('\nSolving second part of puzzle')
stones_count = count_stones('input.raw', blinks_count=75)
print(f'Answer to second part of puzzle is: {stones_count}')
