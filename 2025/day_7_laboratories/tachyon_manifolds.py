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
