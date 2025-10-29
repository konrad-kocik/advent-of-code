def find_santas_floor(input_file_path: str) -> int:
    instructions = _get_instructions(input_file_path)
    return _calculate_floor(instructions)


def _get_instructions(input_file_path: str) -> str:
    with open(input_file_path, 'r') as input_file:
        return input_file.read().strip()


def _calculate_floor(instructions: str) -> int:
    return instructions.count('(') - instructions.count(')')
