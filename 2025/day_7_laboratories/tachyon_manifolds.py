from collections import defaultdict


class TachyonManifolds:
    _START = 'S'
    _BEAM = '|'
    _EMPTY = '.'
    _SPLITTER = '^'

    def __init__(self):
        self._diagram: list[list[str]] = []
        self._quantum_physics = False
        self._beam_splits = 0
        self._timelines = 1

    @property
    def quantum_physics(self) -> bool:
        return self._quantum_physics
    
    @quantum_physics.setter
    def quantum_physics(self, value: bool):
        self._quantum_physics = value

    @property
    def beam_splits(self) -> int:
        return self._beam_splits

    @property
    def timelines(self) -> int:
        return self._timelines

    def load_diagram(self, input_file_path: str):
        with open(input_file_path) as input_file:
            for line in input_file:
                self._diagram.append([char for char in line.strip()])

    def turn_beam_on(self):
        if self._quantum_physics:
            self._track_beam_in_quantum_physics()
        else:
            self._track_beam_in_classical_physics()

    def _track_beam_in_quantum_physics(self):
        streams_in_columns = {x: 1 for x, element in enumerate(self._diagram[0]) if element == self._START}

        for y in range(len(self._diagram[:-1])):
            next_row = self._diagram[y + 1]
            next_streams_in_columns = defaultdict(int)

            for x, streams in streams_in_columns.items():
                if next_row[x] == self._SPLITTER:
                    self._beam_splits += 1
                    self._timelines += streams
                    next_streams_in_columns[x - 1] += streams
                    next_streams_in_columns[x + 1] += streams
                else:
                    next_streams_in_columns[x] += streams

                streams_in_columns = next_streams_in_columns

    def _track_beam_in_classical_physics(self):
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
