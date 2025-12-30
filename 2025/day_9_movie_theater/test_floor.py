from floor import Floor


def test_floor():
    floor = Floor()
    floor.map_red_tiles('test_input.raw')
    assert floor.find_largest_rectangle_area() == 50
