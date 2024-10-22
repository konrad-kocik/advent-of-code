from ticketeer import calculate_ticket_scanning_error_rate, calculate_your_ticket_hash

print('\nSolving first part of puzzle')
ticket_scanning_error_rate = calculate_ticket_scanning_error_rate('input.raw')
print(f'Answer to first part of puzzle is: {ticket_scanning_error_rate}')

print('\nSolving second part of puzzle')
your_ticket_hash = calculate_your_ticket_hash('input.raw')
print(f'Answer to second part of puzzle is: {your_ticket_hash}')
