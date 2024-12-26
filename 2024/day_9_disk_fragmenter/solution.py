from hard_drive import calculate_filesystem_checksum

print('\nSolving first part of puzzle')
filesystem_checksum = calculate_filesystem_checksum('input.raw')
print(f'Answer to first part of puzzle is: {filesystem_checksum}')
