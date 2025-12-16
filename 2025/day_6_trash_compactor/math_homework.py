from math import prod


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

    def read(self, input_file_path: str):
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

    def solve(self) -> int:
        for problem in self._problems:
            problem.solve()

        return sum([problem.result for problem in self._problems])
