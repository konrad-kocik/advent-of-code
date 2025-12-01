from safe import Safe

print('Solving first part of puzzle')
safe = Safe()
safe.input_combination('input.raw')
print(f'Answer to first part of puzzle is: {safe.zeroes_count}')
