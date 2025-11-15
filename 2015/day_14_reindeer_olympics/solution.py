from race import race

print('Solving first part of puzzle')
winner, result = race('input.raw', duration=2503)
print(f'Answer to first part of puzzle is: {winner}, {result}')

print('Solving second part of puzzle')
winner, result = race('input.raw', duration=2503, new_scoring_system=True)
print(f'Answer to second part of puzzle is: {winner}, {result}')
