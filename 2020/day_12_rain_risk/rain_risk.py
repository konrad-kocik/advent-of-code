from navigator import calculate_manhattan_distance, calculate_manhattan_distance_with_waypoint

print('\nSolving first part of puzzle')
manhattan_distance = calculate_manhattan_distance('input.raw')
print(f'Answer to first part of puzzle is: {manhattan_distance}')

print('\nSolving second part of puzzle')
manhattan_distance = calculate_manhattan_distance_with_waypoint('input.raw')
print(f'Answer to second part of puzzle is: {manhattan_distance}')
