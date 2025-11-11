from route_analyzer import find_shortest_route, find_longest_route


def test_find_shortest_route():
    assert find_shortest_route('test_input.raw') == 605


def test_find_longest_route():
    assert find_longest_route('test_input.raw') == 982
