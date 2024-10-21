from handheld_device import get_start_of_packet_marker_position, get_start_of_message_marker_position

print('\nSolving first part of puzzle')
start_of_packet_marker_position = get_start_of_packet_marker_position('input.raw')
print(f'Answer to first part of puzzle is: {start_of_packet_marker_position}')

print('\nSolving second part of puzzle')
start_of_message_marker_position = get_start_of_message_marker_position('input.raw')
print(f'Answer to second part of puzzle is: {start_of_message_marker_position}')
