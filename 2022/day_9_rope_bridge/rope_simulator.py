def count_positions_visited_by_tail(file_path):
    motions = _get_motions(file_path)
    visited_positions = _simulate_motions(motions)
    visited_positions_count = _count_visited_positions(visited_positions)
    return visited_positions_count


def count_positions_visited_by_tail_with_many_knots(file_path):
    motions = _get_motions(file_path)
    visited_positions = _simulate_motions_of_many_knots(motions)
    visited_positions_count = _count_visited_positions(visited_positions)
    return visited_positions_count


def _get_motions(file_path):
    with open(file_path, 'r') as file:
        return [tuple(line.strip().split(' ')) for line in file.readlines()]


def _simulate_motions(motions):
    head_x, head_y = 0, 0
    tail_x, tail_y = 0, 0
    tail_visited = [(tail_x, tail_y)]
    shifts = {'R': (1, 0),
              'L': (-1, 0),
              'U': (0, 1),
              'D': (0, -1)}

    for motion in motions:
        direction, distance = motion
        x_shift, y_shift = shifts[direction]

        for i in range(int(distance)):
            head_x, head_y = _calculate_head_position(head_x, head_y, x_shift, y_shift)
            tail_x, tail_y = _calculate_tail_position(head_x, head_y, tail_x, tail_y, x_shift, y_shift)
            tail_visited.append((tail_x, tail_y))

    return tail_visited


def _simulate_motions_of_many_knots(motions):
    knots_positions = [(0, 0)] * 10

    tail_visited = [knots_positions[9]]
    shifts = {'R': (1, 0),
              'L': (-1, 0),
              'U': (0, 1),
              'D': (0, -1)}

    for motion in motions:
        direction, distance = motion
        x_shift, y_shift = shifts[direction]

        for step in range(int(distance)):
            knots_positions[0] = _calculate_head_position(head_x=knots_positions[0][0], head_y=knots_positions[0][1],
                                                          x_shift=x_shift, y_shift=y_shift)

            for knot in range(1, 10):
                knots_positions[knot] = _calculate_tail_position(head_x=knots_positions[knot-1][0],
                                                                 head_y=knots_positions[knot-1][1],
                                                                 tail_x=knots_positions[knot][0],
                                                                 tail_y=knots_positions[knot][1],
                                                                 x_shift=x_shift,
                                                                 y_shift=y_shift)
            tail_visited.append(knots_positions[9])

    return tail_visited


def _calculate_head_position(head_x, head_y, x_shift, y_shift):
    head_x += x_shift
    head_y += y_shift
    return head_x, head_y


def _calculate_tail_position(head_x, head_y, tail_x, tail_y, x_shift, y_shift):
    # TODO: bug is somewhere here
    if abs(head_x - tail_x) > 1 and head_y == tail_y:
        tail_x += x_shift
    elif abs(head_x - tail_x) > 1 and head_y != tail_y:
        tail_x += x_shift
        tail_y += 1

    if abs(head_y - tail_y) > 1 and head_x == tail_x:
        tail_y += y_shift
    elif abs(head_y - tail_y) > 1 and head_x != tail_x:
        tail_y += y_shift
        tail_x += 1

    return tail_x, tail_y


def _count_visited_positions(visited_positions):
    return len(list(set(visited_positions)))
