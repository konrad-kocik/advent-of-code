class Floor:
    def __init__(self):
        self._red_tiles: list[tuple] = []

    def map_red_tiles(self, input_file_path: str):
        with open(input_file_path) as input_file:
            self._red_tiles = [tuple(map(int, line.strip().split(','))) for line in input_file]


    def find_largest_rectangle_area(self) -> int:
        largest_area = 0

        for first_tile_id, first_tile in enumerate(self._red_tiles):
            first_tile_x, first_tile_y = first_tile

            for second_tile in self._red_tiles[first_tile_id + 1:]:
                second_tile_x, second_tile_y = second_tile
                width = abs(first_tile_x - second_tile_x) + 1
                height = abs(first_tile_y - second_tile_y) + 1
                area = width * height
                largest_area = area if area > largest_area else largest_area

        return largest_area
