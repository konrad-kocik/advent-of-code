from typing import List, Tuple

TopographicMap = List[List[int]]
Coords = Tuple[int, int]
Score = int
Trailhead = Tuple[Coords, Score]
Trailheads = List[Trailhead]


def calculate_sum_of_trailhead_scores(input_file_path: str) -> int:
    topographic_map = _get_topographic_map(input_file_path)
    trailheads = _find_trailheads(topographic_map)
    return _calculate_sum_of_trailheads_scores(trailheads)


def _get_topographic_map(input_file_path: str) -> TopographicMap:
    topographic_map = []

    with open(input_file_path, 'r') as file:
        for line in file:
            row = [int(height) for height in line.strip()]
            topographic_map.append(row)

    return topographic_map


def _find_trailheads(topographic_map: TopographicMap) -> Trailheads:
    trailheads = []

    for y, row in enumerate(topographic_map):
        for x, height in enumerate(row):
            if height == 0:
                trailends_coords = _follow_trail(topographic_map, y, x, trailends_coords=[])
                if trailends_coords:
                    trailheads.append(((y, x), len(trailends_coords)))

    return trailheads


def _follow_trail(topographic_map: TopographicMap, y: int, x: int, trailends_coords: List[Coords]) -> List[Coords]:
    if topographic_map[y][x] == 9:
        if (y, x) not in trailends_coords:
            trailends_coords.append((y, x))
        return trailends_coords

    required_height_for_trail = topographic_map[y][x] + 1

    if y > 0:
        next_y, next_x = y - 1, x
        if topographic_map[next_y][next_x] == required_height_for_trail:
            _follow_trail(topographic_map, next_y, next_x, trailends_coords)

    if x < len(topographic_map[0]) - 1:
        next_y, next_x = y, x + 1
        if topographic_map[next_y][next_x] == required_height_for_trail:
            _follow_trail(topographic_map, next_y, next_x, trailends_coords)

    if y < len(topographic_map) - 1:
        next_y, next_x = y + 1, x
        if topographic_map[next_y][next_x] == required_height_for_trail:
            _follow_trail(topographic_map, next_y, next_x, trailends_coords)

    if x > 0:
        next_y, next_x = y, x - 1
        if topographic_map[next_y][next_x] == required_height_for_trail:
            _follow_trail(topographic_map, next_y, next_x, trailends_coords)

    return trailends_coords


def _calculate_sum_of_trailheads_scores(trailheads: Trailheads) -> int:
    return sum([trailhead[1] for trailhead in trailheads])
