from game import play

print('\nSolving first part of puzzle')
game_result = play(final_turn=2020, numbers=[1, 17, 0, 10, 18, 11, 6])
print(f'Answer to first part of puzzle is: {game_result}')

print('\nSolving second part of puzzle')
game_result = play(final_turn=30000000, numbers=[1, 17, 0, 10, 18, 11, 6])
print(f'Answer to second part of puzzle is: {game_result}')
