from location_finder import calculate_total_distance_between_lists, calculate_lists_similarity_score

print('\nSolving first part of puzzle')
total_distance_between_lists = calculate_total_distance_between_lists('input.raw')
print(f'Answer to first part of puzzle is: {total_distance_between_lists}')

print('\nSolving second part of puzzle')
lists_similarity_score = calculate_lists_similarity_score('input.raw')
print(f'Answer to second part of puzzle is: {lists_similarity_score}')
