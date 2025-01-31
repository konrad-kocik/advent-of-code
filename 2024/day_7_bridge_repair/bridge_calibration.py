from itertools import product
from typing import List, Tuple

Equation = Tuple[int, List[int]]
Equations = List[Equation]


def calculate_total_calibration_result(input_file_path: str, allow_concatenation: bool = False) -> int:
    equations = _get_equations(input_file_path)
    true_equations = _find_true_equations(equations, allow_concatenation)
    return _calculate_sum_of_test_values(true_equations)


def _get_equations(input_file_path: str) -> Equations:
    equations = []

    with open(input_file_path, 'r') as file:
        for line in file:
            test_value, numbers = line.strip().split(': ')
            numbers = [int(number) for number in numbers.split()]
            equations.append((int(test_value), numbers))

    return equations


def _find_true_equations(equations: Equations, allow_concatenation: bool) -> Equations:
    true_equations = []

    for equation in equations:
        if _is_true_equation(equation, allow_concatenation):
            true_equations.append(equation)

    return true_equations


def _is_true_equation(equation: Equation, allow_concatenation: bool) -> bool:
    test_value, numbers = equation
    allowed_operators = ['+', '*', '||'] if allow_concatenation else ['+', '*']
    operators_combinations = list(product(allowed_operators, repeat=len(numbers) - 1))

    for operators in operators_combinations:
        if _calculate_equation(numbers, operators) == test_value:
            return True

    return False


def _calculate_equation(numbers: List[int], operators: Tuple) -> int:
    numbers = numbers.copy()
    result = numbers.pop(0)

    for i, operator in enumerate(operators):
        if operator == '+':
            result += numbers[i]
        if operator == '*':
            result *= numbers[i]
        if operator == '||':
            result = int(str(result) + str(numbers[i]))

    return result


def _calculate_sum_of_test_values(equations: Equations) -> int:
    return sum([equation[0] for equation in equations])
