from lab import count_visited_positions, count_looping_obstacles

print('\nSolving first part of puzzle')
visited_positions_count = count_visited_positions('input.raw')
print(f'Answer to first part of puzzle is: {visited_positions_count}')

print('\nSolving second part of puzzle')
looping_obstacles_count = count_looping_obstacles('input.raw')
print(f'Answer to second part of puzzle is: {count_looping_obstacles}')
