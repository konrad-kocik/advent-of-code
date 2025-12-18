from copy import deepcopy


class TachyonManifolds:
    _START = 'S'
    _BEAM = '|'
    _EMPTY = '.'
    _SPLITTER = '^'

    def __init__(self):
        self._diagram: list[list[str]] = []
        self._beam_splits = 0

    @property
    def beam_splits(self) -> int:
        return self._beam_splits

    def load_diagram(self, input_file_path: str):
        with open(input_file_path) as input_file:
            for line in input_file:
                self._diagram.append([char for char in line.strip()])

    def turn_beam_on(self):
        for y, row in enumerate(self._diagram[:-1]):
            for x, element in enumerate(row):
                if element in (self._START, self._BEAM):
                    downward_element = self._get_downward_element(x, y)
                    if downward_element == self._EMPTY:
                        self._extend_beam(x, y)
                    elif downward_element == self._SPLITTER:
                        self._split_beam(x, y)
                    
    def _get_downward_element(self, x: int, y: int) -> str:
        return self._diagram[y + 1][x]
    
    def _extend_beam(self, x: int, y: int):
        self._diagram[y + 1][x] = self._BEAM

    def _split_beam(self, x: int, y: int):
        self._diagram[y + 1][x - 1] = self._BEAM
        self._diagram[y + 1][x + 1] = self._BEAM
        self._beam_splits += 1


class QuantumTachyonManifolds(TachyonManifolds):
    def __init__(self):
        super().__init__()
        self._timelines = 0

    @property
    def timelines(self) -> int:
        return self._timelines

    def turn_beam_on(self):
        x, y = self._get_starting_coords()
        self._timelines += 1
        self._progress_beam(x, y, self._diagram)

    def _get_starting_coords(self) -> tuple:
        for y, row in enumerate(self._diagram):
            for x, element in enumerate(row):
                if element == self._START:
                    return x, y
        return None, None
    
    def _progress_beam(self, x: int, y: int, diagram: list[list[str]]):
        downward_element = self._get_downward_element(x, y, diagram)
        if downward_element == self._EMPTY:
            self._extend_beam(x, y, diagram)
        elif downward_element == self._SPLITTER:
            self._split_beam(x, y, diagram)

    def _get_downward_element(self, x: int, y: int, diagram: list[list[str]]) -> str:
        return diagram[y + 1][x]

    def _extend_beam(self, x: int, y: int, diagram: list[list[str]]):
        diagram[y + 1][x] = self._BEAM
        # self._show_diagram(diagram)
        if self._can_beam_progress(y, diagram):
            self._progress_beam(x, y + 1, diagram)

    def _split_beam(self, x: int, y: int, diagram: list[list[str]]):  # TODO: refactor this method to eliminate code duplication
        first_diagram = deepcopy(diagram)
        first_diagram[y + 1][x - 1] = self._BEAM
        # self._show_diagram(first_diagram)
        if self._can_beam_progress(y, first_diagram):
            self._progress_beam(x - 1, y + 1, first_diagram)
        del(first_diagram)

        second_diagram = deepcopy(diagram)
        second_diagram[y + 1][x + 1] = self._BEAM
        self._timelines += 1
        # self._show_diagram(second_diagram)
        if self._can_beam_progress(y, second_diagram):
            self._progress_beam(x + 1, y + 1, second_diagram)
        del(second_diagram)

    def _can_beam_progress(self, y: int, diagram: list[list[str]]) -> bool:
        return y < len(diagram) - 2

    def _show_diagram(self, diagram):
        print()
        for row in diagram:
            for element in row:
                print(element, end='')
            print()
        print(self._timelines)
