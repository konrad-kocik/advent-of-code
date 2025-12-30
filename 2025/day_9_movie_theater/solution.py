from floor import Floor

print('Solving first part of puzzle')
floor = Floor()
floor.map_red_tiles('input.raw')
largest_area = floor.find_largest_rectangle_area()
print(f'Answer to first part of puzzle is: {largest_area}')
