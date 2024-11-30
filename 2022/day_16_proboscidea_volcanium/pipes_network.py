from typing import List,Dict, Union

Valves = Dict[str, Dict[str, Union[int, List[str]]]]


def find_maximum_pressure_release(input_file_path: str) -> int:
    valves = _scan_pipes_network(input_file_path)
    return _find_maximum_pressure_release(valves)


def _scan_pipes_network(input_file_path: str) -> Valves:
    valves = {}

    with open(input_file_path, 'r') as file:
        for line in file:
            valve_data, connections_data = line.strip().split('; ')

            name, flow_rate = valve_data.split(' has flow rate=')
            name = name.replace('Valve ', '')
            flow_rate = int(flow_rate)

            connections_data = connections_data.replace('tunnels lead to valves ', '')
            connections_data = connections_data.replace('tunnel leads to valve ', '')
            connected_valves = connections_data.split(', ')

            valves[name] = {'flow_rate': flow_rate, 'connected_valves': connected_valves}

    return valves


def _find_maximum_pressure_release(valves: Valves) -> int:
    pressure_released = 0
    opened_valves_names = []
    time_left = 30
    valve_name = 'AA'

    while time_left > 0:
        valve = valves[valve_name]
        valve_flow_rate = valve['flow_rate']
        print(f'At valve {valve_name} ({valve_flow_rate})')

        time_left -= 1
        pressure_released += (valve_flow_rate * time_left)
        opened_valves_names.append(valve_name)
        print(f'Valve {valve_name} opened')

        time_left -= 1

    return pressure_released
