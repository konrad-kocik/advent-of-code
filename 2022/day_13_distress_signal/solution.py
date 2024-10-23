from decoder import add_up_ids_of_packet_pairs_with_correct_order, calculate_decoder_key

print('\nSolving first part of puzzle')
ids_sum = add_up_ids_of_packet_pairs_with_correct_order('input.raw')
print(f'Answer to first part of puzzle is: {ids_sum}')

print('\nSolving second part of puzzle')
decoder_key = calculate_decoder_key('input.raw', divider_packets=[[[2]], [[6]]])
print(f'Answer to second part of puzzle is: {decoder_key}')
