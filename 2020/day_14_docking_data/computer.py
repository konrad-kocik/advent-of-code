def calculate_memory_sum(file_path):
    program = _get_program(file_path)
    memory = _execute_program(program)
    return _calculate_memory_sum(memory)


def _get_program(file_path):
    with open(file_path, 'r') as file:
        return [tuple(line.strip().split(' = ')) for line in file]


def _execute_program(program):
    memory = {}
    mask = None

    for command, value in program:
        if command == 'mask':
            mask = value
        if 'mem' in command:
            memory[_get_address(command)] = _apply_mask(_convert_to_bits(value), mask)

    return memory


def _convert_to_bits(value):
    return str(bin(int(value))).replace('b', '').zfill(36)


def _apply_mask(value, mask):
    new_value = []

    for position, char in enumerate(mask):
        new_digit = value[position] if char == 'X' else char
        new_value.append(new_digit)

    return ''.join(new_value)


def _get_address(command):
    return command.split('[')[1][:-1]


def _calculate_memory_sum(memory):
    return sum(int(value, 2) for value in memory.values())
