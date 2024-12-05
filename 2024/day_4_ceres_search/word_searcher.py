from typing import List


def search_word(word: str, input_file_path: str) -> int:
    puzzle = _get_puzzle(input_file_path)
    return _search_word_in_puzzle(word, puzzle)


def _get_puzzle(input_file_path: str) -> List[str]:
    puzzle = []

    with open(input_file_path, 'r') as file:
        for line in file:
            puzzle.append(line.strip())

    return puzzle


def _search_word_in_puzzle(word: str, puzzle: List[str]) -> int:
    word_count = 0
    x, y = 0, 0
    max_x = len(puzzle[0]) - 1
    max_y = len(puzzle) - 1

    while y <= max_y:
        while x <= max_x:
            if _can_check_north(word, y):
                word_count += _check_direction(puzzle, word, x, y, direction='N')
            if _can_check_north(word, y) and _can_check_east(puzzle, word, x):
                word_count += _check_direction(puzzle, word, x, y, direction='NE')
            if _can_check_east(puzzle, word, x):
                word_count += _check_direction(puzzle, word, x, y, direction='E')
            if _can_check_south(puzzle, word, y) and _can_check_east(puzzle, word, x):
                word_count += _check_direction(puzzle, word, x, y, direction='SE')
            if _can_check_south(puzzle, word, y):
                word_count += _check_direction(puzzle, word, x, y, direction='S')
            if _can_check_south(puzzle, word, y) and _can_check_west(word, x):
                word_count += _check_direction(puzzle, word, x, y, direction='SW')
            if _can_check_west(word, x):
                word_count += _check_direction(puzzle, word, x, y, direction='W')
            if _can_check_north(word, y) and _can_check_west(word, x):
                word_count += _check_direction(puzzle, word, x, y, direction='NW')
            x += 1

        x = 0
        y += 1

    return word_count


def _can_check_north(word, y):
    return y >= len(word) - 1


def _can_check_east(puzzle, word, x):
    return x <= len(puzzle[0]) - len(word)


def _can_check_south(puzzle, word, y):
    return y <= len(puzzle) - len(word)


def _can_check_west(word, x):
    return x >= len(word) - 1


def _check_direction(puzzle: List[str], word: str, x: int, y: int, direction: str):
    letters_to_check = ''
    shifts = {'N': {'x': 0, 'y': -1},
              'NE': {'x': 1, 'y': -1},
              'E': {'x': 1, 'y': 0},
              'SE': {'x': 1, 'y': 1},
              'S': {'x': 0, 'y': 1},
              'SW': {'x': -1, 'y': 1},
              'W': {'x': -1, 'y': 0},
              'NW': {'x': -1, 'y': -1}}

    for _ in range(len(word)):
        letters_to_check += puzzle[y][x]
        x += shifts[direction]['x']
        y += shifts[direction]['y']

    return 1 if letters_to_check == word else 0
