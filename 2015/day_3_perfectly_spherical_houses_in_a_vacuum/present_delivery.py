Coords = tuple[int, int]


def count_visited_houses(input_file_path: str) -> int:
    directions = _get_directions_from_elf(input_file_path)
    visited_houses = _visit_houses(directions)
    return len(visited_houses)


def _get_directions_from_elf(input_file_path: str) -> str:
    with open(input_file_path, 'r') as input_file:
        return input_file.read().strip()


def _visit_houses(directions: str) -> set[Coords]:
    visited_houses_coords = set()
    current_coords = (0, 0)
    visited_houses_coords.add(current_coords)
    vectors = {'^': (0, 1),
               'v': (0, -1),
               '>': (1, 0),
               '<': (-1, 0)}

    for direction in directions:
        vector = vectors[direction]
        current_coords = (current_coords[0] + vector[0], current_coords[1] + vector[1])
        visited_houses_coords.add(current_coords)

    return visited_houses_coords
