from json import load


def sum_all_numbers(input_file_path: str) -> int:
    content = load(open(input_file_path))
    return _sum_all_numbers(content)


def _sum_all_numbers(content: int | dict | list) -> int:
    result = 0

    if isinstance(content, int):
        result += content
    elif isinstance(content, dict):
        for value in content.values():
            result += _sum_all_numbers(value)
    elif isinstance(content, list):
        for item in content:
            result += _sum_all_numbers(item)

    return result
