from typing import List, Tuple, Dict


def calculate_sum_of_signal_strengths(file_path: str, cycles: List[int]) -> int:
    program = _get_program(file_path)
    cpu_register_history = _calculate_cpu_register_history(program, cycles_count=max(cycles))
    signal_strengths = _get_signal_strengths_at_cycles(cpu_register_history, cycles)
    return sum(signal_strengths)


def render_image(file_path: str) -> List[str]:
    program = _get_program(file_path)
    crt_width = 40
    crt_height = 6
    cpu_register_history = _calculate_cpu_register_history(program, cycles_count=crt_width * crt_height)
    return _render_image_on_crt(cpu_register_history, crt_width, crt_height)


def _get_program(file_path: str) -> List[Tuple]:
    program = []

    with open(file_path, 'r') as file:
        for line in file:
            program.append(tuple(line.strip().split(' ')))

    return program


def _calculate_cpu_register_history(program: List[Tuple], cycles_count: int) -> List[Dict[str, int]]:
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


def _render_image_on_crt(cpu_register_history: List[Dict[str, int]], crt_width: int, crt_height: int) -> List[str]:
    crt_resolution = crt_width * crt_height
    image = []
    line = ''

    for crt_cycle in range(1, crt_resolution + 1):
        pixel_position = crt_width - 1 if crt_cycle % crt_width == 0 else (crt_cycle % crt_width) - 1
        sprite_position = next(event['reg_before'] for event in cpu_register_history if event['cycle'] == crt_cycle)
        sprite_range = (sprite_position - 1, sprite_position, sprite_position + 1)
        line += '#' if pixel_position in sprite_range else '.'

        if crt_cycle % crt_width == 0:
            image.append(line)
            print(line)
            line = ''

    return image


def _get_signal_strengths_at_cycles(register_history: List[Dict[str, int]], cycles: List[int]) -> List[int]:
    return [entry['cycle'] * entry['reg_before'] for entry in register_history if entry['cycle'] in cycles]
