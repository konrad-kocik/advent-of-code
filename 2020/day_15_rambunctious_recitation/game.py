def play(final_turn, numbers):
    last_number = numbers[-1]
    numbers = {number: [turn, None] for turn, number in enumerate(numbers, 1)}
    turn = len(numbers) + 1

    while turn <= final_turn:
        print(f'Turn {turn}')
        last_number = _get_next_number(turn, last_number, numbers)
        _update_numbers(turn, last_number, numbers)
        turn += 1

    return last_number


def _get_next_number(turn, last_number, numbers):
    if last_number not in numbers:
        return 0
    else:
        number_history = numbers[last_number]
        return (turn - 1) - number_history[0] if number_history[1] is None else number_history[0] - number_history[1]


def _update_numbers(turn, number, numbers):
    numbers[number] = [turn, None] if number not in numbers else [turn, numbers[number][0]]
