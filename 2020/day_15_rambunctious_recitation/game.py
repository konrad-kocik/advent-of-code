def play(final_turn, numbers):
    turn = len(numbers) + 1

    while turn <= final_turn:
        numbers.append(_get_number_age(turn, numbers[-1], numbers[:-1]))
        turn += 1

    return numbers[-1]


def _get_number_age(turn, number, numbers):
    return (turn - 1) - _get_last_index_of(number, numbers) if number in numbers else 0


def _get_last_index_of(number, numbers):
    return len(numbers) - numbers[::-1].index(number)
