from maze_solver import MazeSolver

print('\nSolving first part of puzzle')
maze_solver = MazeSolver('input.raw', log_level='debug')
score = maze_solver.score_best_solution(number_of_solutions=100)
print(f'Answer to first part of puzzle is: {score}')


# 20: 285960
# 50: 291960
# 100: 213752
# 100: 263912
# 100: 209704
# 200: 215744
# 200: 225764
# new algorithm
# 50: 133492
# 100: 133492
# 500: 133492
# new algorith (prio)
# 50: 153616
# 100: 153616