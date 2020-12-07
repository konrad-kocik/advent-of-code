def get_highest_seat_id():
    return max(_get_seat_ids())


def get_empty_seat_id():
    seat_ids = _get_seat_ids()
    for i, seat_id in enumerate(seat_ids, start=min(seat_ids)):
        if seat_id != i:
            return i


def _get_seat_ids():
    return sorted(list(map(_get_seat_id, _get_boarding_passes())))


def _get_boarding_passes():
    with open('input.raw', 'r') as file:
        return [line.rstrip() for line in file]


def _get_seat_id(boarding_pass):
    row_id = _decode('FB', boarding_pass[:7], list(range(128)))
    column_id = _decode('LR', boarding_pass[7:], list(range(8)))
    return row_id * 8 + column_id


def _decode(key, code, available_ids):
    go_low, go_high = key
    delimiter = int(len(available_ids) / 2)
    lower_ids = available_ids[:delimiter]
    higher_ids = available_ids[delimiter:]

    if code[0] == go_low:
        return lower_ids[0] if len(code) == 1 else _decode(key, code[1:], lower_ids)
    elif code[0] == go_high:
        return higher_ids[0] if len(code) == 1 else _decode(key, code[1:], higher_ids)


print(get_highest_seat_id())
print(get_empty_seat_id())
