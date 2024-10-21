from game import play_game, play_game_with_new_rules

print('\nSolving first part of puzzle')
score = play_game('input.raw')
print(f'Answer to first part of puzzle is: {score}')

print('\nSolving second part of puzzle')
score = play_game_with_new_rules('input.raw')
print(f'Answer to second part of puzzle is: {score}')
