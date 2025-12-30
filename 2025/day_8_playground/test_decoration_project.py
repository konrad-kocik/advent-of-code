from decoration_project import DecorationProject


def test_decoration_project():
    decoration_project = DecorationProject()
    decoration_project.map_junction_boxes('test_input.raw')
    decoration_project.connect_junction_boxes(count=10)
    assert decoration_project.multiply_sizes_of_largest_circuits(count=3) == 40
