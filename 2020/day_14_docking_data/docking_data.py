from computer import calculate_sum_of_memory, calculate_sum_of_memory_with_floating_addresses

print('\nSolving first part of puzzle')
memory_sum = calculate_sum_of_memory('input.raw')
print(f'Answer to first part of puzzle is: {memory_sum}')

print('\nSolving second part of puzzle')
memory_sum = calculate_sum_of_memory_with_floating_addresses('input.raw')
print(f'Answer to second part of puzzle is: {memory_sum}')
