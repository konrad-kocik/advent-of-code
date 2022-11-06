from seats_arranger import calculate_occupied_seats_for_close_neighbours, \
    calculate_occupied_seats_for_distant_neighbours

print('\nSolving first part of puzzle')
occupied_seats = calculate_occupied_seats_for_close_neighbours('input.raw')
print(f'\nAnswer to first part of puzzle is: {occupied_seats}')

print('\nSolving second part of puzzle')
occupied_seats = calculate_occupied_seats_for_distant_neighbours('input.raw')
print(f'\nAnswer to second part of puzzle is: {occupied_seats}')
