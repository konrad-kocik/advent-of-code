from dataclasses import dataclass


class Actions:
    TURN_ON = 'turn on'
    TURN_OFF = 'turn off'
    TOGGLE = 'toggle'


@dataclass
class Coords:
    x: int
    y: int


@dataclass
class Instruction:
    action: str
    start_coords: Coords
    end_coords: Coords


class Light:
    def __init__(self):
        self._is_on = False

    @property
    def is_on(self) -> bool:
        return self._is_on

    def turn_on(self):
        self._is_on = True

    def turn_off(self):
        self._is_on = False

    def toggle(self):
        self._is_on = not self._is_on

    def show(self):
        color = '93' if self._is_on else '90'
        print(f'\033[{color}m.\033[0m', end='')


class LightsSwitch:
    def __init__(self):
        self._grid = [[Light() for _ in range(1000)] for _ in range(1000)]
        self._instructions = []

    @property
    def lit_lights_count(self) -> int:
        return sum(1 for row in self._grid for light in row if light.is_on)

    def show_grid(self):
        print()

        for row in self._grid:
            for light in row:
                light.show()
            print()

    def load_instructions(self, input_file_path: str):
        with open(input_file_path, 'r') as input_file:
            for line in input_file:
                line = line.strip()

                if line.startswith(Actions.TURN_ON):
                    action = Actions.TURN_ON
                    coords_range = line[len(Actions.TURN_ON) + 1:].strip()
                elif line.startswith(Actions.TURN_OFF):
                    action = Actions.TURN_OFF
                    coords_range = line[len(Actions.TURN_OFF) + 1:].strip()
                elif line.startswith(Actions.TOGGLE):
                    action = Actions.TOGGLE
                    coords_range = line[len(Actions.TOGGLE) + 1:].strip()
                else:
                    raise ValueError(f'Invalid instruction: {line}')

                start_coords, end_coords = coords_range.split(' through ')
                start_coords = Coords(*map(int, start_coords.split(',')))
                end_coords = Coords(*map(int, end_coords.split(',')))

                self._instructions.append(Instruction(action, start_coords, end_coords))

    def execute_instructions(self):
        for instruction in self._instructions:
            lights = [self._grid[x][y] for x in range(instruction.start_coords.x, instruction.end_coords.x + 1)
                                       for y in range(instruction.start_coords.y, instruction.end_coords.y + 1)]

            for light in lights:
                if instruction.action == Actions.TURN_ON:
                    light.turn_on()
                elif instruction.action == Actions.TURN_OFF:
                    light.turn_off()
                elif instruction.action == Actions.TOGGLE:
                    light.toggle()
