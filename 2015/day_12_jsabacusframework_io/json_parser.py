from json import load


def sum_all_numbers(input_file_path: str, ignored_property: str = '') -> int:
    content = load(open(input_file_path))
    return _sum_all_numbers(content, ignored_property)


def _sum_all_numbers(content: int | dict | list, ignored_property: str) -> int:
    result = 0

    if isinstance(content, int):
        result += content
    elif isinstance(content, dict):
        if ignored_property and ignored_property in content.values():
            result += 0
        else:
            for value in content.values():
                result += _sum_all_numbers(value, ignored_property)
    elif isinstance(content, list):
        for item in content:
            result += _sum_all_numbers(item, ignored_property)

    return result
