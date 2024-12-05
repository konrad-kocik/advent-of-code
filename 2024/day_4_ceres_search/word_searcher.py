from typing import List


def search_word(input_file_path: str, mode: str) -> int:
    puzzle = _get_puzzle(input_file_path)
    return _search_word_in_puzzle(puzzle, mode)


def _get_puzzle(input_file_path: str) -> List[str]:
    puzzle = []

    with open(input_file_path, 'r') as file:
        for line in file:
            puzzle.append(line.strip())

    return puzzle


def _search_word_in_puzzle(puzzle: List[str], mode: str) -> int:
    word_count = 0
    x, y = 0, 0
    max_x = len(puzzle[0]) - 1
    max_y = len(puzzle) - 1

    while y <= max_y:
        while x <= max_x:
            if mode == 'XMAS':
                word_count += _search_xmas(puzzle, x, y)
            elif mode == 'X-MAS':
                word_count += _search_x_mas(puzzle, x, y)
            x += 1

        x = 0
        y += 1

    return word_count


def _search_xmas(puzzle: List[str], x: int, y: int) -> int:
    word = 'XMAS'
    count = 0
    
    if _can_check_north(word, y):
        count += 1 if _check_direction(puzzle, x, y, word, direction='N') else 0
    if _can_check_north(word, y) and _can_check_east(puzzle, word, x):
        count += 1 if _check_direction(puzzle, x, y, word,  direction='NE') else 0
    if _can_check_east(puzzle, word, x):
        count += 1 if _check_direction(puzzle, x, y, word, direction='E') else 0
    if _can_check_south(puzzle, word, y) and _can_check_east(puzzle, word, x):
        count += 1 if _check_direction(puzzle, x, y, word, direction='SE') else 0
    if _can_check_south(puzzle, word, y):
        count += 1 if _check_direction(puzzle, x, y, word, direction='S') else 0
    if _can_check_south(puzzle, word, y) and _can_check_west(word, x):
        count += 1 if _check_direction(puzzle, x, y, word, direction='SW') else 0
    if _can_check_west(word, x):
        count += 1 if _check_direction(puzzle, x, y, word, direction='W') else 0
    if _can_check_north(word, y) and _can_check_west(word, x):
        count += 1 if _check_direction(puzzle, x, y, word, direction='NW') else 0

    return count


def _search_x_mas(puzzle: List[str], x: int, y: int) -> int:
    word = '..'
    found = False

    if (_can_check_north(word, y) and
        _can_check_east(puzzle, word, x) and
        _can_check_south(puzzle, word, y) and
        _can_check_west(word, x)):

        found = ((_check_direction(puzzle, x, y, word='AS', direction='NE') and
                  _check_direction(puzzle, x, y, word='AS', direction='SE') and
                  _check_direction(puzzle, x, y, word='AM', direction='SW') and
                  _check_direction(puzzle, x, y, word='AM', direction='NW'))
                 or
                 (_check_direction(puzzle, x, y, word='AM', direction='NE') and
                  _check_direction(puzzle, x, y, word='AS', direction='SE') and
                  _check_direction(puzzle, x, y, word='AS', direction='SW') and
                  _check_direction(puzzle, x, y, word='AM', direction='NW'))
                 or
                 (_check_direction(puzzle, x, y, word='AM', direction='NE') and
                  _check_direction(puzzle, x, y, word='AM', direction='SE') and
                  _check_direction(puzzle, x, y, word='AS', direction='SW') and
                  _check_direction(puzzle, x, y, word='AS', direction='NW'))
                 or
                 (_check_direction(puzzle, x, y, word='AS', direction='NE') and
                  _check_direction(puzzle, x, y, word='AM', direction='SE') and
                  _check_direction(puzzle, x, y, word='AM', direction='SW') and
                  _check_direction(puzzle, x, y, word='AS', direction='NW')))

    return 1 if found else 0


def _can_check_north(word, y):
    return y >= len(word) - 1


def _can_check_east(puzzle, word, x):
    return x <= len(puzzle[0]) - len(word)


def _can_check_south(puzzle, word, y):
    return y <= len(puzzle) - len(word)


def _can_check_west(word, x):
    return x >= len(word) - 1


def _check_direction(puzzle: List[str], x: int, y: int, word: str, direction: str):
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

    return letters_to_check == word
