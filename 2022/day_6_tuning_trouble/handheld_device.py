def get_start_of_packet_marker_position(file_path):
    data_stream = _get_data_stream(file_path)
    marker_position = _find_start_of_packet_marker_position(data_stream)
    return marker_position


def get_start_of_message_marker_position(file_path):
    data_stream = _get_data_stream(file_path)
    marker_position = _find_start_of_message_marker_position(data_stream)
    return marker_position


def _get_data_stream(file_path):
    with open(file_path, 'r') as file:
        return file.read().strip()


def _find_start_of_packet_marker_position(data_stream):
    return _find_marker_position(data_stream, marker_size=4)


def _find_start_of_message_marker_position(data_stream):
    return _find_marker_position(data_stream, marker_size=14)


def _find_marker_position(data_stream, marker_size):
    for position, char in enumerate(data_stream):
        if len(set(data_stream[position:position + marker_size])) == marker_size:
            return position + marker_size
