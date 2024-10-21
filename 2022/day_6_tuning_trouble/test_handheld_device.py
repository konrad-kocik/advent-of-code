from pytest import mark

from handheld_device import get_start_of_packet_marker_position, get_start_of_message_marker_position


@mark.parametrize('file_path, expected_marker_position', [('test_input_1.raw', 7),
                                                          ('test_input_2.raw', 5),
                                                          ('test_input_3.raw', 6),
                                                          ('test_input_4.raw', 10),
                                                          ('test_input_5.raw', 11)])
def test_get_start_of_packet_marker_position(file_path, expected_marker_position):
    assert get_start_of_packet_marker_position(file_path) == expected_marker_position


@mark.parametrize('file_path, expected_marker_position', [('test_input_1.raw', 19),
                                                          ('test_input_2.raw', 23),
                                                          ('test_input_3.raw', 23),
                                                          ('test_input_4.raw', 29),
                                                          ('test_input_5.raw', 26)])
def test_get_start_of_message_marker_position(file_path, expected_marker_position):
    assert get_start_of_message_marker_position(file_path) == expected_marker_position
