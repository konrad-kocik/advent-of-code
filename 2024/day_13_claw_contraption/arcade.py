from typing import List, Dict, Tuple

Coords = Tuple[int, int]
ClawMachineConfig = Dict[str, Coords]


def calculate_minimal_number_of_tokens_to_win_prizes(input_file_path: str) -> int:
    claw_machines_configs = _get_claw_machines_configs(input_file_path)
    valid_button_pushes_for_each_machine = _get_valid_button_pushes_for_each_machine(claw_machines_configs)
    minimum_tokes_to_win_prize_for_each_machine = _get_minimum_tokes_to_win_prize_for_each_machine(valid_button_pushes_for_each_machine)
    return sum(minimum_tokes_to_win_prize_for_each_machine)


def _get_claw_machines_configs(input_file_path: str) -> List[ClawMachineConfig]:
    claw_machines_configs = []

    with open(input_file_path, 'r') as file:
        claw_machine_config = {}

        for line in file:
            line = line.strip()

            if not line:
                claw_machines_configs.append(claw_machine_config)
                claw_machine_config = {}
            else:
                if line.startswith('Button'):
                    button_name, x, y = line.rsplit(maxsplit=2)
                    button_name = button_name[:-1].lower().replace(' ', '_')
                    x = int(x[2:-1])
                    y = int(y[2:])
                    claw_machine_config[button_name] = (x, y)
                elif line.startswith('Prize'):
                    _, x, y = line.split()
                    x = int(x[2:-1])
                    y = int(y[2:])
                    claw_machine_config['prize'] = (x, y)

    claw_machines_configs.append(claw_machine_config)

    return claw_machines_configs


def _get_valid_button_pushes_for_each_machine(claw_machines_configs: List[ClawMachineConfig]) -> List[List[Dict[str, int]]]:
    valid_button_pushes_count_for_each_machine = []

    for claw_machine_config in claw_machines_configs:
        valid_button_pushes_count_for_a_machine = []

        for button_a_pushes_count in range(0, 101):
            for button_b_pushes_count in range(0, 101):
                result_coords = _calculate_result_coords(claw_machine_config, button_a_pushes_count, button_b_pushes_count)

                if result_coords == claw_machine_config['prize']:
                    valid_button_pushes_count_for_a_machine.append({'button_A': button_a_pushes_count,
                                                                    'button_B': button_b_pushes_count})

        valid_button_pushes_count_for_each_machine.append(valid_button_pushes_count_for_a_machine)

    return valid_button_pushes_count_for_each_machine


def _calculate_result_coords(claw_machine_config: ClawMachineConfig, button_a_pushes_count: int, button_b_pushes_count: int):
    button_a_result_coords = (button_a_pushes_count * claw_machine_config['button_a'][0],
                              button_a_pushes_count * claw_machine_config['button_a'][1])
    button_b_result_coords = (button_b_pushes_count * claw_machine_config['button_b'][0],
                              button_b_pushes_count * claw_machine_config['button_b'][1])
    return (button_a_result_coords[0] + button_b_result_coords[0],
            button_a_result_coords[1] + button_b_result_coords[1])


def _get_minimum_tokes_to_win_prize_for_each_machine(valid_button_pushes_for_each_machine: List[List[Dict[str, int]]]) -> List[int]:
    return [_get_minimum_tokes_to_win_prize_for_a_machine(valid_button_pushes_for_a_machine)
            for valid_button_pushes_for_a_machine in valid_button_pushes_for_each_machine
            if valid_button_pushes_for_a_machine]


def _get_minimum_tokes_to_win_prize_for_a_machine(valid_button_pushes_for_a_machine: List[Dict[str, int]]) -> int:
    button_a_cost = 3
    button_b_cost = 1

    return min([button_pushes['button_A'] * button_a_cost + button_pushes['button_B'] * button_b_cost
                for button_pushes in valid_button_pushes_for_a_machine])
