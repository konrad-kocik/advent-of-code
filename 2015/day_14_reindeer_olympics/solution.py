from race import race

print('Solving first part of puzzle')
winner, distance = race('input.raw', duration=2503)
print(f'Answer to first part of puzzle is: {winner}, {distance}')
