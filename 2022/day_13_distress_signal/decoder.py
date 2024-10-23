from typing import List, Dict, Union

Item = Union[int, List]
Packet = List[Item]
PacketsPair = List[Packet]
Signal = List[PacketsPair]

CORRECT_ORDER = 'correct_order'
INCORRECT_ORDER = 'incorrect_order'
UNDETERMINED_ORDER = 'undetermined_order'


def add_up_ids_of_packet_pairs_with_correct_order(input_file_path: str) -> int:
    signal = _get_signal(input_file_path)
    packets_order_correctness = _check_packets_order_correctness(signal)
    return _add_up_ids_of_packet_pairs_with_correct_order(packets_order_correctness)


def _get_signal(input_file_path: str) -> Signal:
    signal = []

    with open(input_file_path, 'r') as file:
        packets_pair = []

        for line in file:
            line = line.strip()

            if line:
                packets_pair.append(eval(line))

            if len(packets_pair) == 2:
                signal.append(packets_pair)
                packets_pair = []

    return signal


def _check_packets_order_correctness(signal: Signal) -> Dict[int, str]:
    packets_order_correctness = {}

    for packets_pair_id, packets_pair in enumerate(signal, start=1):
        left_packet, right_packet = packets_pair
        result = _compare(left_packet, right_packet)
        packets_order_correctness[packets_pair_id] = result

    return packets_order_correctness


def _compare(left_item: Item, right_item: Item) -> str:
    if type(left_item) == int and type(right_item) == int:
        return _compare_integers(left_item, right_item)
    elif type(left_item) == list and type(right_item) == list:
        return _compare_lists(left_item, right_item)
    else:
        left_list = [left_item] if type(left_item) == int else left_item
        right_list = [right_item] if type(right_item) ==  int else right_item
        return _compare_lists(left_list, right_list)


def _compare_integers(left_int: int, right_int: int) -> str:
    if left_int < right_int:
        return CORRECT_ORDER
    elif left_int > right_int:
        return INCORRECT_ORDER
    elif left_int == right_int:
        return UNDETERMINED_ORDER


def _compare_lists(left_list: List, right_list: List) -> str:
    left_list_length, right_list_length = len(left_list), len(right_list)
    shorter_list_length = left_list_length if left_list_length < right_list_length else right_list_length

    for value_id in range(0, shorter_list_length):
        result = _compare(left_list[value_id], right_list[value_id])
        if result == CORRECT_ORDER or result == INCORRECT_ORDER:
            return result

    return _compare_integers(left_list_length, right_list_length)


def _add_up_ids_of_packet_pairs_with_correct_order(packets_order_correctness: Dict[int, str]) -> int:
    return sum([pair_id for pair_id, order in packets_order_correctness.items() if order == CORRECT_ORDER])
