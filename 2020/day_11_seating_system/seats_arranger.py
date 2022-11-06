def calculate_occupied_seats_for_close_neighbours(file_path):
    seats_layout = _get_initial_seats_layout(file_path)
    seats_layout = _arrange_seats_layout_for_close_neighbours(seats_layout)
    return _count_occupied_seats(seats_layout)


def calculate_occupied_seats_for_distant_neighbours(file_path):
    seats_layout = _get_initial_seats_layout(file_path)
    seats_layout = _arrange_seats_layout_for_distant_neighbours(seats_layout)
    return _count_occupied_seats(seats_layout)


def _get_initial_seats_layout(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]


def _arrange_seats_layout_for_close_neighbours(seats_layout):
    _show_seats_layout('Initial', seats_layout)
    everybody_happy = False

    while not everybody_happy:
        everybody_happy = True
        new_seats_layout = seats_layout.copy()

        for row_id, row in enumerate(seats_layout):
            for seat_id, seat in enumerate(row):
                if _should_seat_become_occupied_due_to_close_neighbours(row_id, seat_id, seats_layout):
                    _occupy_seat(row_id, seat_id, new_seats_layout)
                    everybody_happy = False
                    continue
                if _should_seat_become_empty_due_to_close_neighbours(row_id, seat_id, seats_layout):
                    _empty_seat(row_id, seat_id, new_seats_layout)
                    everybody_happy = False
                    continue

        seats_layout = new_seats_layout

    _show_seats_layout('Final', seats_layout)
    return seats_layout


def _arrange_seats_layout_for_distant_neighbours(seats_layout):
    _show_seats_layout('Initial', seats_layout)
    everybody_happy = False

    while not everybody_happy:
        everybody_happy = True
        new_seats_layout = seats_layout.copy()

        for row_id, row in enumerate(seats_layout):
            for seat_id, seat in enumerate(row):
                if _should_seat_become_occupied_due_to_distant_neighbours(row_id, seat_id, seats_layout):
                    _occupy_seat(row_id, seat_id, new_seats_layout)
                    everybody_happy = False
                    continue
                if _should_seat_become_empty_due_to_distant_neighbours(row_id, seat_id, seats_layout):
                    _empty_seat(row_id, seat_id, new_seats_layout)
                    everybody_happy = False
                    continue

        seats_layout = new_seats_layout

    _show_seats_layout('Final', seats_layout)
    return seats_layout


def _should_seat_become_occupied_due_to_close_neighbours(row_id, seat_id, seats_layout):
    seat = seats_layout[row_id][seat_id]

    if seat == '#' or seat == '.':
        return False

    return all(_get_close_neighbouring_empty_seats(row_id, seat_id, seats_layout))


def _should_seat_become_occupied_due_to_distant_neighbours(row_id, seat_id, seats_layout):
    seat = seats_layout[row_id][seat_id]

    if seat == '#' or seat == '.':
        return False

    return all(_get_distant_neighbouring_empty_seats(row_id, seat_id, seats_layout))


def _get_close_neighbouring_empty_seats(row_id, seat_id, seats_layout):
    upper_row = seats_layout[row_id - 1] if row_id > 0 else []
    middle_row = seats_layout[row_id]
    lower_row = seats_layout[row_id + 1] if row_id < len(seats_layout) - 1 else []

    upper_left_empty = upper_row[seat_id - 1] != '#' if upper_row and seat_id > 0 else True
    upper_center_empty = upper_row[seat_id] != '#' if upper_row else True
    upper_right_empty = upper_row[seat_id + 1] != '#' if upper_row and seat_id < len(upper_row) - 1 else True

    middle_left_empty = middle_row[seat_id - 1] != '#' if seat_id > 0 else True
    middle_right_empty = middle_row[seat_id + 1] != '#' if seat_id < len(middle_row) - 1 else True

    lower_left_empty = lower_row[seat_id - 1] != '#' if lower_row and seat_id > 0 else True
    lower_center_empty = lower_row[seat_id] != '#' if lower_row else True
    lower_right_empty = lower_row[seat_id + 1] != '#' if lower_row and seat_id < len(lower_row) - 1 else True

    return (upper_left_empty, upper_center_empty, upper_right_empty,
            middle_left_empty, middle_right_empty,
            lower_left_empty, lower_center_empty, lower_right_empty)


def _get_distant_neighbouring_empty_seats(starting_row_id, starting_seat_id, seats_layout):
    directions = {
        'up_left': {'row_shift': -1, 'seat_shift': -1, 'empty': True},
        'up': {'row_shift': -1, 'seat_shift': 0, 'empty': True},
        'up_right': {'row_shift': -1, 'seat_shift': 1, 'empty': True},
        'left': {'row_shift': 0, 'seat_shift': -1, 'empty': True},
        'right': {'row_shift': 0, 'seat_shift': 1, 'empty': True},
        'down_left': {'row_shift': 1, 'seat_shift': -1, 'empty': True},
        'down': {'row_shift': 1, 'seat_shift': 0, 'empty': True},
        'down_right': {'row_shift': 1, 'seat_shift': 1, 'empty': True}
    }

    min_row_id = 0
    max_row_id = len(seats_layout) - 1
    min_seat_id = 0
    max_seat_id = len(seats_layout[0]) - 1

    for direction_name, direction in directions.items():
        row_id = starting_row_id + direction['row_shift']
        seat_id = starting_seat_id + direction['seat_shift']

        while min_row_id <= row_id <= max_row_id and min_seat_id <= seat_id <= max_seat_id:
            seat = seats_layout[row_id][seat_id]

            if seat == '#':
                direction['empty'] = False
                break

            if seat == 'L':
                direction['empty'] = True
                break

            row_id += direction['row_shift']
            seat_id += direction['seat_shift']

    return tuple(direction['empty'] for direction_name, direction in directions.items())


def _occupy_seat(row_id, seat_id, seats_layout):
    _change_seat_state(row_id, seat_id, seats_layout, new_state='#')


def _change_seat_state(row_id, seat_id, seats_layout, new_state):
    row = seats_layout[row_id]
    new_row = []

    for i, seat in enumerate(row):
        if i == seat_id:
            new_row.append(new_state)
        else:
            new_row.append(seat)

    new_row = ''.join(new_row)
    seats_layout[row_id] = new_row


def _should_seat_become_empty_due_to_close_neighbours(row_id, seat_id, seats_layout):
    seat = seats_layout[row_id][seat_id]

    if seat == 'L' or seat == '.':
        return False

    return _count_close_neighbouring_occupied_seats(row_id, seat_id, seats_layout) >= 4


def _should_seat_become_empty_due_to_distant_neighbours(row_id, seat_id, seats_layout):
    seat = seats_layout[row_id][seat_id]

    if seat == 'L' or seat == '.':
        return False

    return _count_distant_neighbouring_occupied_seats(row_id, seat_id, seats_layout) >= 5


def _count_close_neighbouring_occupied_seats(row_id, seat_id, seats_layout):
    return _get_close_neighbouring_empty_seats(row_id, seat_id, seats_layout).count(False)


def _count_distant_neighbouring_occupied_seats(row_id, seat_id, seats_layout):
    return _get_distant_neighbouring_empty_seats(row_id, seat_id, seats_layout).count(False)


def _empty_seat(row_id, seat_id, seats_layout):
    _change_seat_state(row_id, seat_id, seats_layout, new_state='L')


def _show_seats_layout(stage, seats_layout):
    print(f'\n{stage} seats layout:')

    for row in seats_layout:
        print(row)


def _count_occupied_seats(seats_layout):
    occupied_seats = 0

    for row in seats_layout:
        occupied_seats += row.count('#')

    return occupied_seats
