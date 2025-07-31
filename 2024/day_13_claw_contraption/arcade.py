from typing import List, Dict, Tuple
from sympy import symbols, Eq, solve
from sympy.core.numbers import Integer

Coords = Tuple[int, int]
ClawMachineConfig = Dict[str, Coords]
ButtonsPushCount = Dict[str, int]


def calculate_minimal_number_of_tokens_to_win_prizes(input_file_path: str, unit_conversion: bool = False) -> int:
    claw_machines_configs = _get_claw_machines_configs(input_file_path, unit_conversion)
    buttons_push_count_for_each_machine = _get_buttons_push_count_for_each_machine(claw_machines_configs)
    cost_to_win_prize_for_each_machine = _get_cost_to_win_prize_for_each_machine(buttons_push_count_for_each_machine)
    return sum(cost_to_win_prize_for_each_machine)


def _get_claw_machines_configs(input_file_path: str, unit_conversion: bool) -> List[ClawMachineConfig]:
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

                    if unit_conversion:
                        x, y = x + 10000000000000, y + 10000000000000

                    claw_machine_config['prize'] = (x, y)

    claw_machines_configs.append(claw_machine_config)

    return claw_machines_configs


def _get_buttons_push_count_for_each_machine(claw_machines_configs: List[ClawMachineConfig]) -> List[ButtonsPushCount]:
    return [_get_buttons_push_count_for_a_machine(claw_machine_config) for claw_machine_config in claw_machines_configs]


def _get_buttons_push_count_for_a_machine(claw_machine_config: ClawMachineConfig) -> ButtonsPushCount:
    button_a_x = claw_machine_config['button_a'][0]
    button_a_y = claw_machine_config['button_a'][1]
    button_b_x = claw_machine_config['button_b'][0]
    button_b_y = claw_machine_config['button_b'][1]
    prize_x = claw_machine_config['prize'][0]
    prize_y = claw_machine_config['prize'][1]

    a, b = symbols('a b')
    equations_system = (Eq(button_a_x * a + button_b_x * b, prize_x),
                        Eq(button_a_y * a + button_b_y * b, prize_y))

    solution = solve(equations_system, (a, b))
    a, b = solution[a], solution[b]
    return {'button_a': a, 'button_b': b} if isinstance(a, Integer) and isinstance(b, Integer) else {}


def _get_cost_to_win_prize_for_each_machine(buttons_push_count_for_each_machine: List[ButtonsPushCount]) -> List[int]:
    button_a_cost = 3
    button_b_cost = 1

    return [buttons_push_count['button_a'] * button_a_cost + buttons_push_count['button_b'] * button_b_cost
            for buttons_push_count in buttons_push_count_for_each_machine
            if buttons_push_count]
