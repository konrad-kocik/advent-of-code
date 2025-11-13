def play(sequence: str, repeat: int) -> str:
    for _ in range(repeat):
        sequence = _transform(sequence)
    return sequence


def _transform(sequence: str) -> str:
    transformed = ''
    group = ''
    counter = 0

    for char in sequence:
        if char == group:
            counter += 1
        else:
            if counter != 0:
                transformed += f'{counter}{group}'
                counter = 0
            group = char
            counter += 1

    transformed += f'{counter}{group}'
    return transformed
