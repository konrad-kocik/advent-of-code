from path import find_shortest_path_to_destination


def test_find_shortest_path_to_destination():
    assert find_shortest_path_to_destination('test_input.raw') == 31
