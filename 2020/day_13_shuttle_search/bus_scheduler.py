def calculate_earliest_bus(file_path):
    current_timestamp, bus_ids = _get_bus_schedule(file_path)
    bus_id, time_to_wait = _get_earliest_bus(current_timestamp, bus_ids)
    return bus_id * time_to_wait


def _get_bus_schedule(file_path):
    with open(file_path, 'r') as file:
        lines = [line for line in file]

    departure_timestamp = int(lines[0])
    bus_ids = [int(bus_id) for bus_id in lines[1].split(',') if bus_id != 'x']

    return departure_timestamp, bus_ids


def _get_earliest_bus(current_timestamp, bus_ids):
    nearest_bus_id = None
    shortest_wait_time = None

    for bus_id in bus_ids:
        nearest_bus_departure = (current_timestamp // bus_id) * bus_id

        if nearest_bus_departure >= current_timestamp:
            waiting_time = nearest_bus_departure - current_timestamp
        else:
            waiting_time = nearest_bus_departure + bus_id - current_timestamp

        if nearest_bus_id is None or waiting_time < shortest_wait_time:
            nearest_bus_id = bus_id
            shortest_wait_time = waiting_time

    return nearest_bus_id, shortest_wait_time
