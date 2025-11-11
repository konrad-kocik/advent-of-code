from route_analyzer import find_shortest_route, find_longest_route

print('\nSolving first part of puzzle')
shortest_route = find_shortest_route('input.raw')
print(f'Answer to first part of puzzle is: {shortest_route}')

print('\nSolving second part of puzzle')
longest_route = find_longest_route('input.raw')
print(f'Answer to second part of puzzle is: {longest_route}')
