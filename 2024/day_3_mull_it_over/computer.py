from typing import List
from re import findall


def add_up_results_of_all_instructions_from_memory(input_file_path: str, conditional_statements: bool = False) -> int:
    memory_dump = _dump_memory(input_file_path)
    instructions = _get_valid_instructions(memory_dump, conditional_statements)
    results = _execute_instructions(instructions)
    return sum(results)


def _dump_memory(input_file_path: str) -> str:
    with open(input_file_path, 'r') as file:
        return file.read()


def _get_valid_instructions(memory_dump: str, conditional_statements: bool) -> List[str]:
    pattern = r"don't|do|mul\(\d{1,3},\d{1,3}\)" if conditional_statements else r"mul\(\d{1,3},\d{1,3}\)"
    return findall(pattern, memory_dump)


def _execute_instructions(instructions: List[str]) -> List[int]:
    results = []
    execute = True

    for instruction in instructions:
        if instruction == "don't":
            execute = False
            continue
        elif instruction == "do":
            execute = True
            continue

        if execute:
            x, y = instruction.replace('mul(', '').replace(')', '').split(',')
            results.append(int(x) * int(y))

    return results
