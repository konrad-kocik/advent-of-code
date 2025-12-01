class Safe:
    def __init__(self):
        self._lock_position: int = 50
        self._zeroes_count: int = 0

    @property
    def zeroes_count(self) -> int:
        return self._zeroes_count

    def input_combination(self, input_file_path: str, count_intermediate_zeroes: bool = False):
        with open(input_file_path) as input_file:
            combination = [int(line.strip().replace('L', '-').replace('R', '')) for line in input_file]

        for delta in combination:
            for _ in range(abs(delta)):
                self._lock_position += 1 if delta > 0 else -1

                if self._lock_position == 100:
                    self._lock_position = 0
                
                if self._lock_position == -1:
                    self._lock_position = 99

                self._zeroes_count += 1 if self._lock_position == 0 and count_intermediate_zeroes else 0

            self._zeroes_count += 1 if self._lock_position == 0 and not count_intermediate_zeroes else 0
