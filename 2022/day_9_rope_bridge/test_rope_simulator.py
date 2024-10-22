from rope_simulator import count_positions_visited_by_tail, count_positions_visited_by_tail_with_many_knots


def test_count_positions_visited_by_tail():
    assert count_positions_visited_by_tail('test_input.raw') == 13


def test_count_positions_visited_by_tail_with_many_knots():
    assert count_positions_visited_by_tail_with_many_knots('test_input_2.raw') == 36
