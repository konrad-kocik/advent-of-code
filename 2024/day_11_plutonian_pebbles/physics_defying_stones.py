from typing import List

Stones = List[int]


def count_stones(input_file_path: str, blinks_count: int) -> int:
    stones = _examine_stones(input_file_path)
    stones = _blink(stones, blinks_count=blinks_count)
    return len(stones)


def _examine_stones(input_file_path: str) -> Stones:
    with open(input_file_path, 'r') as file:
        return [int(stone) for stone in file.readline().split()]


def _blink(stones: Stones, blinks_count: int) -> Stones:
    for _ in range(blinks_count):
        changed_stones = []

        for stone in stones:
            if stone == 0:
                changed_stones.append(1)
            elif len(str(stone)) % 2 == 0:
                stone = str(stone)
                left_half_of_digits, right_half_of_digits = stone[:len(stone) // 2], stone[len(stone) // 2:]
                changed_stones.append(int(left_half_of_digits))
                changed_stones.append(int(right_half_of_digits))
            else:
                changed_stones.append(stone * 2024)

        stones = changed_stones

    return changed_stones
