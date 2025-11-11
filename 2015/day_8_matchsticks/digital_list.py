def calculate_code_representation_overhead(input_file_path: str) -> int:
    strings = _get_strings(input_file_path)
    memory_representation_size = _calculate_memory_representation_size(strings)
    code_representation_size = _calculate_code_representation_size(strings)
    return code_representation_size - memory_representation_size


def _get_strings(input_file_path: str) -> list[str]:
    strings = []

    with open(input_file_path, 'r') as input_file:
        for string in input_file:
            strings.append(f'{string.strip()}')

    return strings


def _calculate_memory_representation_size(strings: list[str]) -> int:
    return sum([len(eval(f'{string}')) for string in strings])


def _calculate_code_representation_size(strings: list[str]) -> int:
    return sum([len(string) for string in strings])
