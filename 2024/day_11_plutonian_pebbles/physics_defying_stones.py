from typing import List, Dict

Stones = List[int]


def count_stones(input_file_path: str, blinks_count: int) -> int:
    stones = _examine_stones(input_file_path)
    return _blink(stones, blinks_count=blinks_count)


def _examine_stones(input_file_path: str) -> Stones:
    with open(input_file_path, 'r') as file:
        return [int(stone) for stone in file.readline().split()]


def _blink(stones: Stones, blinks_count: int) -> int:
    special_stones = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    special_stones_blinks_left = {}

    for blink_id in range(blinks_count):
        print(f'Blink ID {blink_id}')
        changed_stones = []

        for stone in stones:
            if stone in special_stones:
                if stone in special_stones_blinks_left:
                    special_stones_blinks_left[stone].append(blinks_count - blink_id)
                else:
                    special_stones_blinks_left[stone] = [blinks_count - blink_id]
            elif len(str(stone)) % 2 == 0:
                stone = str(stone)
                left_half_of_digits, right_half_of_digits = stone[:len(stone) // 2], stone[len(stone) // 2:]
                changed_stones.append(int(left_half_of_digits))
                changed_stones.append(int(right_half_of_digits))
            else:
                changed_stones.append(stone * 2024)

        stones = changed_stones
        print(f'Stones count {len(stones)}')

    return _count_stones(stones, special_stones_blinks_left)


def _unfold_stones(stone: int, stones_blinks_left: List[int]) -> int:
    print(f'Blinks left for {stone} stones count: {len(stones_blinks_left)}')
    blink_count = max(stones_blinks_left)
    stones = [stone]
    stones_count = 0

    for blink_id in range(1, blink_count + 1):
        print(f'Blink ID {blink_id}')
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

        for blinks_left in stones_blinks_left:
            if blinks_left == blink_id:
                stones_count += len(stones)

    return stones_count


def _count_stones(stones: Stones, stones_blinks_left: Dict[int, List[int]]) -> int:
    stones_count = len(stones)

    for stone in stones_blinks_left:
        stones_count += _unfold_stones(stone=stone, stones_blinks_left=stones_blinks_left[stone])

    return stones_count
