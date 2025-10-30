from present_delivery import count_visited_houses

print('\nSolving first part of puzzle')
visited_houses_count = count_visited_houses('input.raw')
print(f'Answer to first part of puzzle is: {visited_houses_count}')

print('\nSolving second part of puzzle')
visited_houses_count = count_visited_houses('input.raw', robot_santa_deployed=True)
print(f'Answer to second part of puzzle is: {visited_houses_count}')
