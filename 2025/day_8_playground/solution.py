from decoration_project import DecorationProject

print('Solving first part of puzzle')
decoration_project = DecorationProject()
decoration_project.map_junction_boxes('input.raw')
decoration_project.connect_junction_boxes(count=1000)
result = decoration_project.multiply_sizes_of_largest_circuits(count=3)
print(f'Answer to first part of puzzle is: {result}')
