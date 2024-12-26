from copy import deepcopy
from typing import Dict, Tuple, List

LabMap = Dict[int, Dict[int, str]]


def count_visited_positions(input_file_path: str) -> int:
    lab_map = _create_lab_map(input_file_path)
    _simulate_patrol(lab_map)
    return _count_visited_tiles(lab_map)


def count_looping_obstacles(input_file_path: str) -> int:
    lab_map = _create_lab_map(input_file_path)
    lab_maps_with_looping_guard = _simulate_patrols_with_additional_obstacle(lab_map)
    return len(lab_maps_with_looping_guard)


def _create_lab_map(input_file_path: str) -> LabMap:
    tiles = {}

    with open(input_file_path, 'r') as file:
        for y, line in enumerate(file.readlines(), start=0):
            row = {}
            line = line.strip()

            for x, tile in enumerate(line, start=0):
                row[x] = tile

            tiles[y] = row

    return tiles


def _simulate_patrol(lab_map: LabMap):
    guard_movement = {'^': (-1, 0),
                      'V': (1, 0),
                      '>': (0, 1),
                      '<': (0, -1)}
    y, x, guard_direction = _find_guard(lab_map)

    while not _is_guard_on_edge(lab_map, y, x):
        y_shift, x_shift = guard_movement[guard_direction]
        new_y = y + y_shift
        new_x = x + x_shift

        if lab_map[new_y][new_x] == '#':
            guard_direction = _change_guard_direction(guard_direction)
            continue

        lab_map[y][x] = 'X'
        lab_map[new_y][new_x] = guard_direction
        y, x = new_y, new_x


def _simulate_patrols_with_additional_obstacle(lab_map: LabMap) -> List[LabMap]:
    lab_maps_with_additional_obstacle = _create_lab_maps_with_additional_obstacle(lab_map)
    print(f'Maps count: {len(lab_maps_with_additional_obstacle)}')
    lab_maps_with_looping_guard = []

    for i, lab_map_with_additional_obstacle in enumerate(lab_maps_with_additional_obstacle):
        print(f'Checking map {i}')
        if _does_guard_loop(lab_map_with_additional_obstacle):
            print(f'Guard does loop on map {i}')
            lab_maps_with_looping_guard.append(lab_map_with_additional_obstacle)

    return lab_maps_with_looping_guard


def _create_lab_maps_with_additional_obstacle(lab_map: LabMap) -> List[LabMap]:
    lab_maps_with_additional_obstacle = []

    for y, row in lab_map.items():
        for x, tile in row.items():
            if lab_map[y][x] == '.':
                print(f'Adding obstacle to {y}, {x}')
                lab_map_with_additional_obstacle = deepcopy(lab_map)
                lab_map_with_additional_obstacle[y][x] = '#'
                lab_maps_with_additional_obstacle.append(lab_map_with_additional_obstacle)

    return lab_maps_with_additional_obstacle


def _does_guard_loop(lab_map: LabMap) -> bool:
    guard_movement = {'^': (-1, 0),
                      'V': (1, 0),
                      '>': (0, 1),
                      '<': (0, -1)}
    y, x, guard_direction = _find_guard(lab_map)
    steps = []

    while not _is_guard_on_edge(lab_map, y, x):
        y_shift, x_shift = guard_movement[guard_direction]
        new_y = y + y_shift
        new_x = x + x_shift

        if lab_map[new_y][new_x] == '#':
            guard_direction = _change_guard_direction(guard_direction)
            continue

        lab_map[y][x] = 'X'
        lab_map[new_y][new_x] = guard_direction
        step = ((y, x), (new_y, new_x))
        steps.append(step)
        y, x = new_y, new_x

        if _have_loop(steps):
            print(f'Loop detected')
            return True

    return False


def _find_guard(lab_map: LabMap) -> Tuple[int, int, str]:
    for y, row in lab_map.items():
        for x, tile in row.items():
            if tile in ('^', 'V', '<', '>'):
                return y, x, tile


def _is_guard_on_edge(lab_map: LabMap, y: int, x: int) -> bool:
    return y == 0 or x == 0 or y == len(lab_map) - 1 or x == len(lab_map[0]) - 1


def _change_guard_direction(current_direction: str) -> str:
    new_directions = {'^': '>',
                      'V': '<',
                      '>': 'V',
                      '<': '^'}

    return new_directions[current_direction]


def _count_visited_tiles(lab_map: LabMap) -> int:
    visited_tiles_count = 0

    for row in lab_map.values():
        for tile in row.values():
            if tile == 'X' or tile in ('^', 'V', '<', '>'):
                visited_tiles_count += 1

    return visited_tiles_count


def _have_loop(steps: List[Tuple[Tuple[int, int], Tuple[int, int]]]) -> bool:
    for step in steps:
        if steps.count(step) > 1:
            return True

    return False
