from typing import Tuple, List, Optional

WarehouseMap = List[List[str]]
RobotMovements = str
Coords = Tuple[int, int]
Vector = Tuple[int, int]

ROBOT = '@'
BOX = 'O'
EMPTY_SPACE = '.'
WALL = '#'


def calculate_boxes_gps_coords_sum_after_robot_movements(input_file_path: str) -> int:
    warehouse_map, robot_movements = _get_data_from_lanternfish(input_file_path)
    warehouse_map = _simulate_robot_movements(warehouse_map, robot_movements)
    return _calculate_boxes_gps_coords_sum(warehouse_map)


def _get_data_from_lanternfish(input_file_path: str) -> Tuple[WarehouseMap, RobotMovements]:
    warehouse_map = []
    robot_movements = ''
    section = 'warehouse_map'

    with open(input_file_path, 'r') as file:
        for line in file:
            line = line.strip()

            if not line:
                section = 'robot_movements'
                continue

            if section == 'warehouse_map':
                warehouse_map.append([*line])
            elif section == 'robot_movements':
                robot_movements = robot_movements + line

    return warehouse_map, robot_movements


def _simulate_robot_movements(warehouse_map: WarehouseMap, robot_movements: RobotMovements) -> WarehouseMap:
    movement_vectors = {'^': (0, -1),
                        '>': (1, 0),
                        'v': (0, 1),
                        '<': (-1, 0)}

    for robot_movement in robot_movements:
        movement_vector = movement_vectors[robot_movement]
        _move_robot(warehouse_map, movement_vector)

    return warehouse_map


def _move_robot(warehouse_map: WarehouseMap, movement_vector: Vector):
    robot_coords = _get_robot_coords(warehouse_map)
    _try_to_move(robot_coords, movement_vector, warehouse_map)


def _get_robot_coords(warehouse_map: WarehouseMap) -> Optional[Coords]:
    for y, row in enumerate(warehouse_map):
        for x, char in enumerate(row):
            if char == ROBOT:
                return x, y
    return None


def _try_to_move(start_coords: Coords, vector: Vector, warehouse_map: WarehouseMap) -> bool:
    target_coords = (start_coords[0] + vector[0],
                     start_coords[1] + vector[1])
    target_char = _get_char_from_warehouse_map(target_coords, warehouse_map)

    if target_char == WALL:
        return False
    elif target_char == EMPTY_SPACE:
        _move_char_on_warehouse_map(start_coords, target_coords, warehouse_map)
        return True
    elif target_char == BOX:
        moved = _try_to_move(target_coords, vector, warehouse_map)
        if moved:
            _move_char_on_warehouse_map(start_coords, target_coords, warehouse_map)
        return moved
    else:
        return False


def _get_char_from_warehouse_map(coords: Coords, warehouse_map: WarehouseMap) -> str:
    return warehouse_map[coords[1]][coords[0]]


def _move_char_on_warehouse_map(source_coords: Coords, target_coords: Coords, warehouse_map: WarehouseMap):
    char_to_move = _get_char_from_warehouse_map(source_coords, warehouse_map)
    warehouse_map[target_coords[1]][target_coords[0]] = char_to_move
    warehouse_map[source_coords[1]][source_coords[0]] = EMPTY_SPACE


def _calculate_boxes_gps_coords_sum(warehouse_map: WarehouseMap) -> int:
    boxes_gps_coords_sum = 0

    for y, row in enumerate(warehouse_map):
        for x, char in enumerate(row):
            if char == BOX:
                boxes_gps_coords_sum += 100 * y + x

    return boxes_gps_coords_sum
