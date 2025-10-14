from typing import Tuple, List, Optional

WarehouseMap = List[List[str]]
RobotMovements = str
Coords = Tuple[int, int]
Vector = Tuple[int, int]


class Warehouse:
    _ROBOT = '@'
    _BOX = 'O'
    _BIG_BOX = '[]'
    _BIG_BOX_LEFT_SIDE = _BIG_BOX[0]
    _BIG_BOX_RIGHT_SIDE = _BIG_BOX[1]
    _EMPTY_SPACE = '.'
    _WALL = '#'

    _VECTORS = {'^': (0, -1),
                '>': (1, 0),
                'v': (0, 1),
                '<': (-1, 0)}

    def __init__(self, input_file_path: str, double_width: bool = False):
        self._input_file_path: str = input_file_path
        self._double_width: bool = double_width
        warehouse_map, robot_movements = self._get_data_from_lanternfish()
        self._warehouse_map: WarehouseMap = warehouse_map
        self._robot_movements: RobotMovements = robot_movements

    def calculate_boxes_gps_coords_sum_after_robot_movements(self) -> int:
        self._simulate_robot_movements()
        return self._calculate_boxes_gps_coords_sum()

    def _get_data_from_lanternfish(self) -> Tuple[WarehouseMap, RobotMovements]:
        warehouse_map = []
        robot_movements = ''
        section = 'warehouse_map'

        with open(self._input_file_path, 'r') as file:
            for line in file:
                line = line.strip()

                if not line:
                    section = 'robot_movements'
                    continue

                if section == 'warehouse_map':
                    map_row = self._prepare_map_row(line)
                    warehouse_map.append(map_row)

                elif section == 'robot_movements':
                    robot_movements = robot_movements + line

        return warehouse_map, robot_movements

    def _prepare_map_row(self, line: str) -> List[str]:
        map_row = []

        for read_char in line:
            if read_char == self._ROBOT:
                new_chars = [self._ROBOT, self._EMPTY_SPACE] if self._double_width else [self._ROBOT]
            elif read_char == self._BOX:
                new_chars = [self._BIG_BOX_LEFT_SIDE, self._BIG_BOX_RIGHT_SIDE] if self._double_width else self._BOX
            elif read_char == self._EMPTY_SPACE:
                new_chars = [self._EMPTY_SPACE, self._EMPTY_SPACE] if self._double_width else [self._EMPTY_SPACE]
            elif read_char == self._WALL:
                new_chars = [self._WALL, self._WALL] if self._double_width else [self._WALL]
            else:
                new_chars = []

            map_row.extend(new_chars)

        return map_row

    def _simulate_robot_movements(self):
        self._show_map()

        for robot_movement in self._robot_movements:
            print(f'\nTrying to move robot {robot_movement}')
            robot_coords = self._get_robot_coords()
            vector = self._VECTORS[robot_movement]
            movable = self._check_if_movable(robot_coords, vector)

            if movable:
                print(f'Moving robot {robot_movement}')
                self._move(robot_coords, vector)
            else:
                print(f'Cannot move robot {robot_movement}')

            self._show_map()

    def _show_map(self):
        print()

        for row in self._warehouse_map:
            print(' '.join(row))

    def _get_robot_coords(self) -> Optional[Coords]:
        for y, row in enumerate(self._warehouse_map):
            for x, char in enumerate(row):
                if char == self._ROBOT:
                    return x, y
        return None

    def _check_if_movable(self, source_coords: Coords, vector: Vector) -> bool:
        target_coords = (source_coords[0] + vector[0],
                         source_coords[1] + vector[1])
        target_char = self._get_char_from_warehouse_map(target_coords)
        movable = False

        if target_char == self._EMPTY_SPACE:
            movable = True
        elif target_char == self._BOX:
            movable = self._check_if_movable(target_coords, vector)
        elif target_char in self._BIG_BOX:
            movable = self._check_if_movable(target_coords, vector)
            if movable and (vector == self._VECTORS['^'] or vector == self._VECTORS['v']):
                big_box_other_half_coords = (target_coords[0] + 1 if target_char == self._BIG_BOX_LEFT_SIDE else target_coords[0] - 1,
                                             target_coords[1])
                movable = self._check_if_movable(big_box_other_half_coords, vector)

        return movable

    def _get_char_from_warehouse_map(self, coords: Coords) -> str:
        return self._warehouse_map[coords[1]][coords[0]]

    def _move(self, source_coords: Coords, vector: Vector):
        target_coords = (source_coords[0] + vector[0],
                         source_coords[1] + vector[1])
        target_char = self._get_char_from_warehouse_map(target_coords)

        if target_char == self._EMPTY_SPACE:
            self._replace_char_on_warehouse_map(source_coords, target_coords)
        elif target_char == self._BOX:
            self._move(target_coords, vector)
            self._replace_char_on_warehouse_map(source_coords, target_coords)
        elif target_char in self._BIG_BOX:
            self._move(target_coords, vector)
            self._replace_char_on_warehouse_map(source_coords, target_coords)
            if vector == self._VECTORS['^'] or vector == self._VECTORS['v']:
                big_box_other_half_coords = (target_coords[0] + 1 if target_char == self._BIG_BOX_LEFT_SIDE else target_coords[0] - 1,
                                             target_coords[1])
                self._move(big_box_other_half_coords, vector)

    def _replace_char_on_warehouse_map(self, source_coords: Coords, target_coords: Coords):
        char_to_move = self._get_char_from_warehouse_map(source_coords)
        self._warehouse_map[target_coords[1]][target_coords[0]] = char_to_move
        self._warehouse_map[source_coords[1]][source_coords[0]] = self._EMPTY_SPACE

    def _calculate_boxes_gps_coords_sum(self) -> int:
        boxes_gps_coords_sum = 0

        for y, row in enumerate(self._warehouse_map):
            for x, char in enumerate(row):
                if char == self._BOX or char == self._BIG_BOX_LEFT_SIDE:
                    boxes_gps_coords_sum += 100 * y + x

        return boxes_gps_coords_sum
