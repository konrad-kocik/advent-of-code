from decoder import add_up_ids_of_packet_pairs_with_correct_order


def test_add_up_ids_of_packet_pairs_with_correct_order():
    assert add_up_ids_of_packet_pairs_with_correct_order('test_input.raw') == 13
