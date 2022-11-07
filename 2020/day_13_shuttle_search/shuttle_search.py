from bus_scheduler import calculate_earliest_bus

print('\nSolving first part of puzzle')
earliest_bus_hash = calculate_earliest_bus('input.raw')
print(f'Answer to first part of puzzle is: {earliest_bus_hash}')
