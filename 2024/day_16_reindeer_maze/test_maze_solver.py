from maze_solver import MazeSolver


def test_score_best_solution_for_small_maze():
    maze_solver = MazeSolver('test_input_1.raw', log_level='debug')
    assert maze_solver.score_best_solution(number_of_solutions=10) == 7036

def test_score_best_solution_for_big_maze():
    maze_solver = MazeSolver('test_input_2.raw', log_level='debug')
    assert maze_solver.score_best_solution(number_of_solutions=20) == 11048
