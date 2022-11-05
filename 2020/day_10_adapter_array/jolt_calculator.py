import itertools


def calculate_jolt_differences(file_path):
    adapters = sorted(_get_adapters(file_path))
    differences = {}

    for adapter_id, adapter in enumerate(adapters):
        difference = adapter if adapter_id == 0 else adapter - adapters[adapter_id - 1]
        _update_differences(differences, difference)

    _add_device_to_differences(differences)

    return differences


def _get_adapters(file_path):
    with open(file_path, 'r') as file:
        return [int(line.strip()) for line in file]


def _update_differences(differences, difference):
    if differences.get(difference):
        differences[difference] += 1
    else:
        differences[difference] = 1


def _add_device_to_differences(differences):
    _update_differences(differences, 3)
