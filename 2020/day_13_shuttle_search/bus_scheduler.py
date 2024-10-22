from datetime import datetime


def calculate_earliest_bus_hash(file_path):
    current_timestamp, bus_ids = _get_bus_schedule(file_path)
    bus_id, time_to_wait = _get_earliest_bus(current_timestamp, bus_ids)
    return bus_id * time_to_wait


def find_sequential_bus_departure_timestamp(file_path, starting_timestamp=0):
    _, bus_ids = _get_bus_schedule(file_path)
    earliest_departure_window_start = _find_sequential_bus_departure_timestamp(bus_ids, starting_timestamp)
    return earliest_departure_window_start


def _get_bus_schedule(file_path):
    with open(file_path, 'r') as file:
        lines = [line for line in file]

    departure_timestamp = int(lines[0])
    bus_ids = [bus_id for bus_id in lines[1].split(',')]

    return departure_timestamp, bus_ids


def _get_earliest_bus(current_timestamp, bus_ids):
    nearest_bus_id = None
    shortest_wait_time = None

    for bus_id in bus_ids:
        if bus_id == 'x':
            continue

        bus_id = int(bus_id)
        nearest_bus_departure = (current_timestamp // bus_id) * bus_id

        if nearest_bus_departure >= current_timestamp:
            waiting_time = nearest_bus_departure - current_timestamp
        else:
            waiting_time = nearest_bus_departure + bus_id - current_timestamp

        if nearest_bus_id is None or waiting_time < shortest_wait_time:
            nearest_bus_id = bus_id
            shortest_wait_time = waiting_time

    return nearest_bus_id, shortest_wait_time


def _find_sequential_bus_departure_timestamp(bus_ids, starting_timestamp=0):
    timestamp = starting_timestamp
    found = False
    start_time = datetime.now()

    while not found:
        print(f'Checking timestamp {timestamp}')

        for offset, bus_id in enumerate(bus_ids):
            if bus_id == 'x':
                found = True
                continue
            if not _check_timestamp(timestamp, offset, int(bus_id)):
                found = False
                timestamp += int(bus_ids[0])
                break
            else:
                found = True
                continue

    print(f'Search time {datetime.now() - start_time}')
    return timestamp


def _check_timestamp(timestamp, offset, bus_id):
    return (timestamp + offset) % bus_id == 0
