from typing import List, Dict, Union
from math import prod

Item = Union[int, List]
Packet = List[Item]
PacketsPair = List[Packet]
Signal = List[Union[PacketsPair, Packet]]

CORRECT_ORDER = 'correct_order'
INCORRECT_ORDER = 'incorrect_order'
UNDETERMINED_ORDER = 'undetermined_order'


def add_up_ids_of_packet_pairs_with_correct_order(input_file_path: str) -> int:
    signal = _get_signal(input_file_path, pair_packets=True)
    packets_order_correctness = _check_packets_order_correctness(signal)
    return _add_up_ids_of_packet_pairs_with_correct_order(packets_order_correctness)


def calculate_decoder_key(input_file_path: str, divider_packets: PacketsPair) -> int:
    signal = _get_signal(input_file_path, pair_packets=False)
    signal = _add_divider_packets(signal, divider_packets)
    signal = _sort_packets(signal)
    return _calculate_decoder_key(signal, divider_packets)


def _get_signal(input_file_path: str, pair_packets: bool) -> Signal:
    signal = []

    with open(input_file_path, 'r') as file:
        packets_pair = []

        for line in file:
            line = line.strip()

            if line and not pair_packets:
                signal.append(eval(line))

            if line and pair_packets:
                packets_pair.append(eval(line))

                if len(packets_pair) == 2:
                    signal.append(packets_pair)
                    packets_pair = []

    return signal


def _add_divider_packets(signal: Signal, divider_packets: PacketsPair) -> Signal:
    signal.extend(divider_packets)
    return signal


def _check_packets_order_correctness(signal: Signal) -> Dict[int, str]:
    packets_order_correctness = {}

    for packets_pair_id, packets_pair in enumerate(signal, start=1):
        left_packet, right_packet = packets_pair
        result = _compare(left_packet, right_packet)
        packets_order_correctness[packets_pair_id] = result

    return packets_order_correctness


def _sort_packets(signal: Signal) -> Signal:
    sorted_signal = []

    for packet in signal:
        result = UNDETERMINED_ORDER

        for sorted_packet_id, sorted_packet in enumerate(sorted_signal):
            result = _compare(packet, sorted_packet)
            if result == CORRECT_ORDER:
                sorted_signal.insert(sorted_packet_id, packet)
                break

        if result != CORRECT_ORDER:
            sorted_signal.append(packet)

    return sorted_signal


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


def _calculate_decoder_key(signal: Signal, divider_packets: PacketsPair) -> int:
    return prod([packet_id for packet_id, packet in enumerate(signal, start=1) if packet in divider_packets])
