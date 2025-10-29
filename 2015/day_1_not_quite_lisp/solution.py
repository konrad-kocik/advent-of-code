from building import find_santas_floor, wait_for_santa_in_basement

print('\nSolving first part of puzzle')
floor_number = find_santas_floor('input.raw')
print(f'Answer to first part of puzzle is: {floor_number}')

print('\nSolving second part of puzzle')
instruction_number = wait_for_santa_in_basement('input.raw')
print(f'Answer to second part of puzzle is: {instruction_number}')
