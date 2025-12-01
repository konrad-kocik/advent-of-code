class Safe:
    def __init__(self):
        self._lock_position: int = 50
        self._zeroes_count: int = 0

    @property
    def zeroes_count(self) -> int:
        return self._zeroes_count

    def input_combination(self, input_file_path: str):
        with open(input_file_path) as input_file:
            combination = [int(line.strip().replace('L', '-').replace('R', '')) for line in input_file]

        for move in combination:
            self._lock_position = (self._lock_position + move) % 100
            self._zeroes_count += 1 if self._lock_position == 0 else 0
