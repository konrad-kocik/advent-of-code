from decoder import add_up_ids_of_packet_pairs_with_correct_order, calculate_decoder_key


def test_add_up_ids_of_packet_pairs_with_correct_order():
    assert add_up_ids_of_packet_pairs_with_correct_order('test_input.raw') == 13


def test_calculate_decoder_key():
    assert calculate_decoder_key('test_input.raw', divider_packets=[[[2]], [[6]]]) == 140
