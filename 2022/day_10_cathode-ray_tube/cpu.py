from typing import List, Tuple, Dict


def calculate_sum_of_signal_strengths(file_path: str, cycles: List[int]) -> int:
    program = _get_program(file_path)
    register_history = _calculate_register_history(program, cycles_count=max(cycles))
    signal_strengths = _get_signal_strengths_at_cycles(register_history, cycles)
    return sum(signal_strengths)


def _get_program(file_path: str) -> List[Tuple]:
    program = []

    with open(file_path, 'r') as file:
        for line in file:
            program.append(tuple(line.strip().split(' ')))

    return program


def _calculate_register_history(program: List[Tuple], cycles_count: int) -> List[Dict[str, int]]:
    cycle = 0
    reg = 1
    history = []

    for instruction in program:
        if instruction[0] == 'noop':
            cycle += 1
            history.append({'cycle': cycle, 'reg_before': reg, 'reg_after': reg})
        elif instruction[0] == 'addx':
            cycle += 1
            history.append({'cycle': cycle, 'reg_before': reg, 'reg_after': reg})
            cycle += 1
            reg_before = reg
            reg += int(instruction[1])
            history.append({'cycle': cycle, 'reg_before': reg_before, 'reg_after': reg})
        if cycle >= cycles_count:
            break

    return history


def _get_signal_strengths_at_cycles(register_history: List[Dict[str, int]], cycles: List[int]) -> List[int]:
    return [entry['cycle'] * entry['reg_before'] for entry in register_history if entry['cycle'] in cycles]
