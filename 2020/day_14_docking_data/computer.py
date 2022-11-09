def calculate_sum_of_memory(file_path):
    program = _get_program(file_path)
    memory = _execute_program(program)
    return _calculate_memory_sum(memory)


def calculate_sum_of_memory_with_floating_addresses(file_path):
    program = _get_program(file_path)
    memory = _execute_program_in_memory_with_floating_addresses(program)
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
            memory[_get_address(command)] = _apply_mask_to_value(_convert_to_bits(value), mask)

    return memory


def _execute_program_in_memory_with_floating_addresses(program):
    memory = {}
    mask = None

    for command, value in program:
        if command == 'mask':
            mask = value
        if 'mem' in command:
            for address in _get_addresses(command, mask):
                memory[address] = _convert_to_bits(value)

    return memory


def _convert_to_bits(value):
    return str(bin(int(value))).replace('b', '').zfill(36)


def _apply_mask_to_value(value, mask):
    masked_values = []

    for position, mask_bit in enumerate(mask):
        value_bit = value[position] if mask_bit == 'X' else mask_bit
        masked_values.append(value_bit)

    return ''.join(masked_values)


def _apply_mask_to_address(address, mask):
    masked_address = []

    for position, mask_bit in enumerate(mask):
        address_bit = address[position] if mask_bit == '0' else mask_bit
        masked_address.append(address_bit)

    return ''.join(masked_address)


def _get_address(command):
    return command.split('[')[1][:-1]


def _get_addresses(command, mask):
    return _get_addresses_permutations(_apply_mask_to_address(_convert_to_bits(_get_address(command)), mask))


def _get_addresses_permutations(masked_address):
    addresses = []

    for bits in _get_bits_permutations(masked_address.count('X')):
        address = masked_address

        for bit in bits:
            address = address.replace('X', bit, 1)

        addresses.append(address)

    return addresses


def _get_bits_permutations(floating_bit_count):
    return [str(bin(number)).replace('0b', '').zfill(floating_bit_count) for number in range(2 ** floating_bit_count)]


def _calculate_memory_sum(memory):
    return sum(int(value, 2) for value in memory.values())
