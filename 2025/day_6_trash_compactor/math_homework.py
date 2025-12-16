from math import prod
from collections import defaultdict


class MathProblem:
    def __init__(self):
        self._operands: list[int] = []
        self._operator: str = ''
        self._result: int = 0

    @property
    def operator(self) -> str:
        return self._operator

    @operator.setter
    def operator(self, operator: str):
        self._operator = operator

    @property
    def result(self) -> int:
        return self._result

    def add_operand(self, operand: int):
        self._operands.append(operand)

    def solve(self):
        self._result = sum(self._operands) if self._operator == '+' else prod(self._operands)


class MathHomework:
    def __init__(self):
        self._problems: list[MathProblem] = []

    def read(self, input_file_path: str, cephalopod_math: bool = False):
        if cephalopod_math:
            self._read_using_cephalopod_math(input_file_path)
        else:
            self._read_using_classical_math(input_file_path)

    def solve(self) -> int:
        for problem in self._problems:
            problem.solve()

        return sum([problem.result for problem in self._problems])

    def _read_using_cephalopod_math(self, input_file_path: str):
        operands = self._read_cephalopod_operands(input_file_path)
        operators = self._read_cephalopod_operators(input_file_path)
        self._create_cephalopod_math_problems(operands, operators)

    def _read_cephalopod_operands(self, input_file_path: str) -> dict[int, int | None]:
        operands = defaultdict(str)

        with open(input_file_path) as input_file:
            lines = input_file.readlines()

        for line in lines[:-1]:
            line = line[:-1]

            for column_id, char in enumerate(line[::-1]):
                operands[column_id] += char

        return {operand_id: int(operand) if operand.strip() else None for operand_id, operand in operands.items()}

    def _read_cephalopod_operators(self, input_file_path: str) -> dict[int, str | None]:
        operators = {}

        with open(input_file_path) as input_file:
            lines = input_file.readlines()

        for column_id, char in enumerate(lines[-1][::-1]):
            operators[column_id] = char if char else None

        return operators

    def _create_cephalopod_math_problems(self, operands: dict[int, int | None], operators: dict[int, str | None]):
        problem_operands = {}

        for column_id, operand in operands.items():
            if operand:
                problem_operands[column_id] = operand
            else:
                self._create_cephalopod_math_problem(problem_operands, operators)
                problem_operands.clear()
                continue  

        if problem_operands:
            self._create_cephalopod_math_problem(problem_operands, operators)

    def _create_cephalopod_math_problem(self, problem_operands: dict[int, int], operators: dict[int, str | None]):
        problem = MathProblem()

        for column_id, problem_operand in problem_operands.items():
            problem.add_operand(problem_operand)

            if operator := operators[column_id]:
                problem.operator = operator

        self._problems.append(problem)

    def _read_using_classical_math(self, input_file_path: str):
        with open(input_file_path) as input_file:
            for line in input_file:
                line = line.strip()

                if not self._problems:
                    for operand in line.split():
                        problem = MathProblem()
                        problem.add_operand(int(operand))
                        self._problems.append(problem)
                else:
                    line_parts = line.split()

                    if line_parts[0].isnumeric():
                        for problem_id, operand in enumerate(line_parts):
                            self._problems[problem_id].add_operand(int(operand))
                    else:
                        for problem_id, operator in enumerate(line_parts):
                            self._problems[problem_id].operator = operator
