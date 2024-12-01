from typing import Tuple, List


def calculate_total_distance_between_lists(input_file_path: str) -> int:
    left_list, right_list = _get_lists(input_file_path)
    distances_between_locations = _calculate_distances_between_locations(left_list, right_list)
    return sum(distances_between_locations)


def _get_lists(input_file_path: str) -> Tuple[List, List]:
    left_list, right_list = [], []

    with open(input_file_path, 'r') as file:
        for line in file:
            left_location_id, right_location_id = line.strip().split()
            left_list.append(int(left_location_id))
            right_list.append(int(right_location_id))

    return left_list, right_list


def _calculate_distances_between_locations(left_list: List[int], right_list: List[int]) -> List[int]:
    location_id_pairs = zip(sorted(left_list), sorted(right_list))
    return [abs(left_location_id - right_location_id) for left_location_id, right_location_id in location_id_pairs]
