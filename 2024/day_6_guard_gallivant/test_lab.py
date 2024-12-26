from lab import count_visited_positions, count_looping_obstacles


def test_count_visited_positions():
    assert count_visited_positions('test_input.raw') == 41


def test_count_looping_obstacles():
    assert count_looping_obstacles('test_input.raw') == 6
