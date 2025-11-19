class Light:
    def __init__(self, x: int, y: int, is_on: bool):
        self._x = x
        self._y = y
        self._is_on = is_on

    @property
    def x(self) -> int:
        return self._x

    @property
    def y(self) -> int:
        return self._y

    @property
    def is_on(self) -> bool:
        return self._is_on

    def turn_on(self):
        self._is_on = True


Grid = list[list[Light]]


class LightsSwitch:
    def __init__(self):
        self._grid: Grid = []

    @property
    def grid_height(self) -> int:
        return len(self._grid)

    @property
    def grid_width(self) -> int:
        return len(self._grid[0])

    @property
    def lit_lights_count(self) -> int:
        return sum(1 for row in self._grid for light in row if light.is_on)

    def configure(self, input_file_path: str):
        with open(input_file_path) as input_file:
            for y, line in enumerate(input_file):
                row = [Light(x, y, is_on=(char == '#')) for x, char in enumerate(line.strip())]
                self._grid.append(row)

    def animate(self, steps: int, corner_lights_stuck: bool = False):
        for _ in range(steps):
            self._turn_on_corner_lights() if corner_lights_stuck else None
            self._grid = [[Light(light.x, light.y, is_on=self._is_updated_light_on(light)) for light in row] for row in self._grid]
        self._turn_on_corner_lights() if corner_lights_stuck else None

    def _turn_on_corner_lights(self):
        corner_lights = [self._grid[0][0],
                         self._grid[0][-1],
                         self._grid[-1][0],
                         self._grid[-1][-1]]
        
        for corner_light in corner_lights:
            corner_light.turn_on()

    def _is_updated_light_on(self, light: Light) -> bool:
        neighbours_turned_on = 0

        for x_shift in (-1, 0, 1):
            for y_shift in (-1, 0, 1):
                if not x_shift == y_shift == 0:
                    neighbour_x = light.x + x_shift
                    neighbour_y = light.y + y_shift

                    if self._is_inside_grid(neighbour_x, neighbour_y):
                        neighbour = self._grid[neighbour_y][neighbour_x]
                        neighbours_turned_on += 1 if neighbour.is_on else 0

        if light.is_on:
            return neighbours_turned_on == 2 or neighbours_turned_on == 3
        else:
            return neighbours_turned_on == 3

    def _is_inside_grid(self, x: int, y: int) -> bool:
        return (y >= 0 and
                y < self.grid_height and
                x >= 0 and
                x <self.grid_width)
