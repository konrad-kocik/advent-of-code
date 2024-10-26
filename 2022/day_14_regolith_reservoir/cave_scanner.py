from typing import Tuple, List, Any, Optional, Type, Dict

Coords = Tuple[int, int]
LineCoords = Tuple[Coords, Coords]
TilesMatrix = Dict[int, Dict[int, 'Tile']]


class TileContent:
    @property
    def symbol(self) -> str:
        raise NotImplemented()


class Air(TileContent):
    @property
    def symbol(self) -> str:
        return '.'


class Rock(TileContent):
    @property
    def symbol(self) -> str:
        return '#'


class Sand(TileContent):
    @property
    def symbol(self) -> str:
        return '+'


class RestingSand(TileContent):
    @property
    def symbol(self) -> str:
        return 'o'


class Tile:
    def __init__(self, x: int, y: int, content: Any):
        self._x = x
        self._y = y
        self._content = content

    @property
    def x(self) -> int:
        return self._x

    @property
    def y(self) -> int:
        return self._y

    @property
    def content(self) -> TileContent:
        return self._content

    @content.setter
    def content(self, value):
        self._content = value

    @property
    def printable_content(self):
        return self._content.symbol


class CaveMap:
    def __init__(self, rocks_coords: List[LineCoords]):
        self._tiles = self._generate_tiles(rocks_coords)

    def show(self):
        print('\n')

        for y in sorted(self._tiles.keys()):
            row = self._tiles[y]
            printable_row = ''

            for x in sorted(row.keys()):
                printable_row += row[x].printable_content

            print(printable_row)

    def set_tile(self, coords: Coords, tile_content: TileContent):
        tile = self._get_tile(coords)

        if tile:
            tile.content = tile_content

    def is_tile_blocked(self, coords: Coords) -> bool:
        tile = self._get_tile(coords)
        return tile and (type(tile.content) == Rock or type(tile.content) == RestingSand)

    def tile_exists(self, coords: Coords) -> bool:
        return bool(self._get_tile(coords))

    def count_tiles_with(self, content_type: Type[TileContent]) -> int:
        tile_count = 0

        for row in self._tiles.values():
            for tile in row.values():
                if type(tile.content) == content_type:
                    tile_count += 1

        return tile_count

    def _generate_tiles(self, rocks_coords: List[LineCoords]) -> TilesMatrix:
        min_x, max_x, min_y, max_y = _get_cave_edges(rocks_coords)
        tiles = {}

        for y in range(min_y, max_y + 1):
            row = {}

            for x in range(min_x, max_x + 1):
                tile_content = Rock() if self._should_tile_be_a_rock(x, y, rocks_coords) else Air()
                row[x] = Tile(x, y, tile_content)

            tiles[y] = row

        return tiles

    def _get_tile(self, coords) -> Optional[Tile]:
        x, y = coords
        return self._tiles.get(y).get(x)


    @staticmethod
    def _should_tile_be_a_rock(tile_x, tile_y, rocks_coords):
        for rock_coords in rocks_coords:
            rock_start_coords, rock_end_coords = rock_coords
            rock_start_x, rock_start_y = rock_start_coords
            rock_end_x, rock_end_y = rock_end_coords

            collinear = ((tile_y - rock_start_y) * (rock_end_x - rock_start_x) ==
                         (rock_end_y - rock_start_y) * (tile_x - rock_start_x))
            within_bounds = (min(rock_start_x, rock_end_x) <= tile_x <= max(rock_start_x, rock_end_x) and
                             min(rock_start_y, rock_end_y) <= tile_y <= max(rock_start_y, rock_end_y))

            if collinear and within_bounds:
                return True

        return False


def count_units_of_resting_sand_after_simulation(input_file_path: str, include_floor: bool = False, visualize: bool = False) -> int:
    cave_map = _scan_cave(input_file_path, include_floor)
    _simulate_sand_pouring(cave_map, visualize)
    return cave_map.count_tiles_with(RestingSand)


def _scan_cave(input_file_path: str, include_floor: bool) -> CaveMap:
    rocks_coords = []

    with open(input_file_path, 'r') as file:
        for line in file:
            line = line.strip()
            coords_from_line = line.split(' -> ')
            rock_coords = []

            for coords in coords_from_line:
                x, y = coords.split(',')
                rock_coords.append((int(x), int(y)))

                if len(rock_coords) == 2:
                    rocks_coords.append((rock_coords[0], rock_coords[1]))
                    rock_coords = [rock_coords[1]]

    if include_floor:
        min_x, max_x, min_y, max_y = _get_cave_edges(rocks_coords)
        floor_coords = ((min_x - max_y, max_y + 2), (max_x + max_y, max_y + 2))
        rocks_coords.append(floor_coords)

    return CaveMap(rocks_coords)


def _get_cave_edges(rocks_coords: List[LineCoords]) -> Tuple[int, int, int, int]:
    min_x, max_x, min_y, max_y = None, None, 0, None

    for rock_coords in rocks_coords:
        for coords in rock_coords:
            x, y = coords
            min_x = x if min_x is None or x < min_x else min_x
            max_x = x if max_x is None or x > max_x else max_x
            max_y = y if max_y is None or y > max_y else max_y

    return min_x, max_x, min_y, max_y


def _simulate_sand_pouring(cave_map: CaveMap, visualize: bool):
    sand_source_coords = (500, 0)
    should_be_pouring = True

    while should_be_pouring:
        current_coords = sand_source_coords
        cave_map.set_tile(current_coords, Sand())
        cave_map.show() if visualize else None

        while True:
            prev_coords = current_coords
            down_coords = (prev_coords[0], prev_coords[1] + 1)
            left_coords = (prev_coords[0] - 1, prev_coords[1] + 1)
            right_coords = (prev_coords[0] + 1, prev_coords[1] + 1)

            if not cave_map.is_tile_blocked(down_coords):
                current_coords = down_coords
            elif not cave_map.is_tile_blocked(left_coords):
                current_coords = left_coords
            elif not cave_map.is_tile_blocked(right_coords):
                current_coords = right_coords
            else:
                _rest_sand(cave_map, prev_coords, visualize)
                if prev_coords == sand_source_coords:
                    should_be_pouring = False
                break

            if cave_map.tile_exists(current_coords):
                _move_sand(cave_map, current_coords, prev_coords, visualize)
            else:
                cave_map.set_tile(prev_coords, Air())
                should_be_pouring = False
                break

    cave_map.show()


def _move_sand(cave_map: CaveMap, next_coords: Coords, prev_coords: Coords, visualize: bool):
    cave_map.set_tile(next_coords, Sand())
    cave_map.set_tile(prev_coords, Air())
    cave_map.show() if visualize else None


def _rest_sand(cave_map: CaveMap, coords: Coords, visualize: bool):
    cave_map.set_tile(coords, RestingSand())
    cave_map.show() if visualize else None
