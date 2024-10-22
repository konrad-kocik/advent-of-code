from typing import Tuple, List, Dict, Union
from math import floor

MonkeysState = List[List[int]]
MonkeyBehaviour = Dict[str, Dict[str, Union[str, int]]]
MonkeysBehaviour = List[MonkeyBehaviour]
MonkeysStats = Dict[int, int]


def calculate_level_of_monkey_business(input_file_path: str, rounds: int):
    monkeys_state, monkeys_behaviour = _observe_monkeys(input_file_path)
    monkeys_state, monkeys_stats = _simulate_monkey_business(monkeys_state, monkeys_behaviour, rounds)
    monkeys_stats_sorted = list(sorted(monkeys_stats.values()))
    return monkeys_stats_sorted[-2] * monkeys_stats_sorted[-1]


def _observe_monkeys(input_file_path: str) -> Tuple[MonkeysState, MonkeysBehaviour]:
    monkeys_state = []
    monkeys_behaviour = []

    with open(input_file_path, 'r') as file:
        for line in file:
            line = line.strip()

            if line and 'Starting items:' in line:
                _add_monkey_state(line, monkeys_state)
                continue

            if line and 'Operation:' in line:
                monkey_behaviour = {}
                _add_operation_to_monkey_behaviour(line, monkey_behaviour)
                continue

            if line and 'Test:' in line:
                _add_test_to_monkey_behaviour(line, monkey_behaviour)
                continue

            if line and 'If true:' in line:
                _add_positive_test_result_to_monkey_behaviour(line, monkey_behaviour)
                continue

            if line and 'If false:' in line:
                _add_negative_test_result_to_monkey_behaviour(line, monkey_behaviour)
                monkeys_behaviour.append(monkey_behaviour)
                continue

    return monkeys_state, monkeys_behaviour


def _add_monkey_state(line: str, monkeys_state: MonkeysState):
    _, items = line.split(': ')
    monkey_state = list(map(int, items.split(', ')))
    monkeys_state.append(monkey_state)


def _add_operation_to_monkey_behaviour(line: str, monkey_behaviour: MonkeyBehaviour):
    operator, value = None, None

    if '* old' in line:
        operator = '^'
        value = None
    elif '*' in line:
        operator = '*'
        value = int(line.split(' * ')[-1])
    elif '+' in line:
        operator = '+'
        value = int(line.split(' + ')[-1])

    monkey_behaviour['operation'] = {'operator': operator, 'value': value}


def _add_test_to_monkey_behaviour(line: str, monkey_behaviour: MonkeyBehaviour):
    value = int(line.split()[-1])
    monkey_behaviour['test'] = {'value': value}


def _add_positive_test_result_to_monkey_behaviour(line: str, monkey_behaviour: MonkeyBehaviour):
    if_true = int(line.split()[-1])
    monkey_behaviour['test']['if_true'] = if_true


def _add_negative_test_result_to_monkey_behaviour(line: str, monkey_behaviour: MonkeyBehaviour):
    if_false = int(line.split()[-1])
    monkey_behaviour['test']['if_false'] = if_false


def _simulate_monkey_business(monkeys_state: MonkeysState, monkeys_behaviour: MonkeysBehaviour, rounds: int) -> Tuple[MonkeysState, MonkeysStats]:
    monkeys = monkeys_state.copy()
    monkeys_stats = {monkey_id: 0 for monkey_id in range(0, len(monkeys_state))}

    for _ in range(1, rounds + 1):
        for monkey_id, monkey in enumerate(monkeys):
            for item in monkey.copy():
                monkeys_stats[monkey_id] += 1
                behaviour = monkeys_behaviour[monkey_id]
                item = _calculate_item_value(item, behaviour['operation']['operator'], behaviour['operation']['value'])
                target_monkey_id = _get_target_monkey_id(item, behaviour['test'])
                monkey.pop(0)
                monkeys[target_monkey_id].append(item)

    return monkeys_state, monkeys_stats


def _calculate_item_value(item: int, operator: str, value: int) -> int:
    if operator == '+':
        item += value
    elif operator == '*':
        item *= value
    elif operator == '^':
        item *= item

    return int(floor(item / 3))


def _get_target_monkey_id(item: int, test: Dict) -> int:
    return test['if_true'] if item % test['value'] == 0 else test['if_false']
