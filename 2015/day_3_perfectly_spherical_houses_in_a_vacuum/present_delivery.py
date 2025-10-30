Coords = tuple[int, int]

VECTORS = {'^': (0, 1),
           'v': (0, -1),
           '>': (1, 0),
           '<': (-1, 0)}


def count_visited_houses(input_file_path: str, robot_santa_deployed: bool = False) -> int:
    directions = _get_directions_from_elf(input_file_path)
    visited_houses = _visit_houses_with_robot_santa(directions) if robot_santa_deployed else _visit_houses(directions)
    return len(visited_houses)


def _get_directions_from_elf(input_file_path: str) -> str:
    with open(input_file_path, 'r') as input_file:
        return input_file.read().strip()


def _visit_houses_with_robot_santa(directions: str) -> set[Coords]:
    santa_visited_houses = _visit_houses(directions[::2])
    robot_santa_visited_houses = _visit_houses(directions[1::2])
    return santa_visited_houses.union(robot_santa_visited_houses)


def _visit_houses(directions: str) -> set[Coords]:
    visited_houses_coords = set()
    current_coords = (0, 0)
    visited_houses_coords.add(current_coords)

    for direction in directions:
        vector = VECTORS[direction]
        current_coords = (current_coords[0] + vector[0], current_coords[1] + vector[1])
        visited_houses_coords.add(current_coords)

    return visited_houses_coords
