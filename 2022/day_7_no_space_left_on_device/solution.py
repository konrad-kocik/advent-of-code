from handheld_device import get_total_size_of_small_dirs, get_total_size_of_smallest_dir_to_delete

print('\nSolving first part of puzzle')
total_size_of_small_dirs = get_total_size_of_small_dirs('input.raw')
print(f'Answer to first part of puzzle is: {total_size_of_small_dirs}')

print('\nSolving second part of puzzle')
total_size_of_smallest_dir_to_delete = get_total_size_of_smallest_dir_to_delete('input.raw')
print(f'Answer to second part of puzzle is: {total_size_of_smallest_dir_to_delete}')
