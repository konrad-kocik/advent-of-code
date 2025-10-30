def count_nice_strings(input_file_path: str) -> int:
    strings = _get_strings(input_file_path)
    return len(_find_nice_strings(strings))


def _get_strings(input_file_path: str) -> list[str]:
    with open(input_file_path, 'r') as file:
        return [line.strip() for line in file]


def _find_nice_strings(strings: list[str]) -> list[str]:
    return [string for string in strings if _is_nice(string)]


def _is_nice(string: str) -> bool:
    return (_has_three_vowels(string) and
            _has_double_letter(string) and
            not _has_forbidden_substrings(string))


def _has_three_vowels(string: str) -> bool:
    vowels_count = sum([1 for char in string if char in 'aeiou'])
    return vowels_count >= 3


def _has_double_letter(string: str) -> bool:
    for char_id, char in enumerate(string[:-1]):
        if char == string[char_id + 1]:
            return True
    return False


def _has_forbidden_substrings(string: str) -> bool:
    return any(forbidden_substring in string for forbidden_substring in ['ab', 'cd', 'pq', 'xy'])
