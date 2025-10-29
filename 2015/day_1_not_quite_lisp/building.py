from typing import Optional


def find_santas_floor(input_file_path: str) -> int:
    instructions = _get_instructions(input_file_path)
    return _calculate_floor(instructions)


def wait_for_santa_in_basement(input_file_path: str) -> Optional[int]:
    instructions = _get_instructions(input_file_path)
    return _get_instruction_number_for_basement(instructions)


def _get_instructions(input_file_path: str) -> str:
    with open(input_file_path, 'r') as input_file:
        return input_file.read().strip()


def _calculate_floor(instructions: str) -> int:
    return instructions.count('(') - instructions.count(')')


def _get_instruction_number_for_basement(instructions: str) -> Optional[int]:
    floor = 0

    for instruction_index, instruction in enumerate(instructions, start=1):
        floor += 1 if instruction == '(' else -1

        if floor == -1:
            return instruction_index

    return None
