class PrintingDepartment:
    ROLL_OF_PAPER = '@'
    EMPTY_CELL = '.'

    def __init__(self):
        self._map: list[list[str]] = []

    def load_map(self, input_file_path: str):
        with open(input_file_path) as input_file:
            for line in input_file:
                self._map.append([cell for cell in line])

    def count_accessable_rolls_of_paper(self) -> int:
        accessable_rolls_of_paper_count = 0

        for y, row in enumerate(self._map):
            for x, cell in enumerate(row):
                accessable_rolls_of_paper_count += 1 if cell == self.ROLL_OF_PAPER and self._is_accessable(x, y) else 0

        return accessable_rolls_of_paper_count

    def remove_rolls_of_paper_until_inaccessable(self) -> int:
        removed_rolls_of_paper_count = 0

        while accessable_rolls_of_paper_coords := self._get_accessable_rolls_of_paper_coords():
            for x, y in accessable_rolls_of_paper_coords:
                self._remove_roll_of_paper(x, y)
                removed_rolls_of_paper_count += 1

        return removed_rolls_of_paper_count

    def _get_accessable_rolls_of_paper_coords(self) -> list[tuple[int, int]]:
        accessable_rolls_of_paper_coords = []

        for y, row in enumerate(self._map):
            for x, cell in enumerate(row):
                if cell == self.ROLL_OF_PAPER and self._is_accessable(x, y):
                    accessable_rolls_of_paper_coords.append((x, y))

        return accessable_rolls_of_paper_coords

    def _is_accessable(self, x: int, y: int) -> bool:
        neighbouring_rolls_of_paper_count = 0

        for coords_shift in [(0, 1),
                             (1, 1),
                             (1, 0),
                             (1, -1),
                             (0, -1),
                             (-1, -1),
                             (-1, 0),
                             (-1, 1)]:
            neighbouring_cell_coords = (x + coords_shift[0],
                                        y + coords_shift[1])
            neighbouring_cell = self._get_cell(*neighbouring_cell_coords)
            neighbouring_rolls_of_paper_count += 1 if neighbouring_cell and neighbouring_cell == self.ROLL_OF_PAPER else 0
        
        return neighbouring_rolls_of_paper_count < 4

    def _get_cell(self, x: int, y: int) -> str | None:
        if y >= 0 and y < len(self._map) and x >= 0 and x < len(self._map[y]):
            return self._map[y][x]

    def _remove_roll_of_paper(self, x: int, y: int):
        self._map[y][x] = self.EMPTY_CELL
