from itertools import combinations


def count_possible_containers_combinations(input_file_path: str, eggnog_amount: int) -> int:
    containers = _get_containers(input_file_path)
    possible_containers_combinations = _find_possible_containers_combinations(containers, eggnog_amount)
    return len(possible_containers_combinations)


def _get_containers(input_file_path: str) -> list[int]:
    with open(input_file_path) as input_file:
        return [int(line) for line in input_file]


def _find_possible_containers_combinations(containers: list[int], eggnog_amount: int) -> list[list[int]]:
    possible_containers_combinations = []
    containers_count = len(containers)

    for containers_count_in_combination in range(1, containers_count + 1):
        for containers_ids in combinations(range(containers_count), containers_count_in_combination):
            containers_total_capcity = sum([containers[container_id] for container_id in containers_ids])

            if containers_total_capcity == eggnog_amount:
                possible_containers_combinations.append(containers_ids)

    return possible_containers_combinations
