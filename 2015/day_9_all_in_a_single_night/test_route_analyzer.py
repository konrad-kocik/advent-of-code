from route_analyzer import find_shortest_route


def test_find_shortest_route():
    assert find_shortest_route('test_input.raw') == 605
