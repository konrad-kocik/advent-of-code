from typing import List


class Stone:
    def __init__(self, base_value: int, multiplier: int = 1):
        self.base_value = base_value
        self.multiplier = multiplier

    def __repr__(self):
        return str(self.base_value * self.multiplier)

    @property
    def number_engraved(self) -> int:
        return self.base_value * self.multiplier


def count_stones(input_file_path: str, blinks_count: int) -> int:
    stones = _examine_stones(input_file_path)
    return _blink(stones, blinks_count=blinks_count)


def _examine_stones(input_file_path: str) -> List[Stone]:
    with open(input_file_path, 'r') as file:
        return [Stone(int(number)) for number in file.readline().split()]


def _blink(stones: List[Stone], blinks_count: int) -> List[Stone]:
    zero_stones_count = 0

    for blink_id in range(blinks_count):
        print(f'Blink {blink_id + 1}')
        changed_stones = []

        for stone in stones:
            if stone.number_engraved == 0:
                zero_stones_count += 1
            elif len(str(stone.number_engraved)) % 2 == 0:
                stone = str(stone.number_engraved)
                left_half_of_digits, right_half_of_digits = stone[:len(stone) // 2], stone[len(stone) // 2:]
                changed_stones.append(Stone(int(left_half_of_digits)))
                changed_stones.append(Stone(int(right_half_of_digits)))
            else:
                stone.multiplier *= 2024
                changed_stones.append(stone)

        stones = changed_stones

    print(f'Basic stones count: {len(stones)}')

    return len(stones) + _unfold_zero_stones(zero_stones_count, blinks_count)


def _unfold_zero_stones(zero_stones_count: int, blinks_count: int):
    # print(f'Zero stones count: {zero_stones_count}')
    stones = [Stone(0)]
    print(stones)

    for blink_id in range(blinks_count):
        changed_stones = []

        for stone in stones:
            if stone.number_engraved == 0:
                changed_stones.append(Stone(1))
            elif len(str(stone.number_engraved)) % 2 == 0:
                stone = str(stone.number_engraved)
                left_half_of_digits, right_half_of_digits = stone[:len(stone) // 2], stone[len(stone) // 2:]
                changed_stones.append(Stone(int(left_half_of_digits)))
                changed_stones.append(Stone(int(right_half_of_digits)))
            else:
                stone.multiplier *= 2024
                changed_stones.append(stone)

        stones = changed_stones
        print(stones)

    # print(f'Zero stone unfolds to: {len(stones)}')
    # print(f'Zero stones count: {len(stones) * zero_stones_count}')
    return len(stones) * zero_stones_count
