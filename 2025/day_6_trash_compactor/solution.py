from math_homework import MathHomework

print('Solving first part of puzzle')
math_homework = MathHomework()
math_homework.read('input.raw')
result = math_homework.solve()
print(f'Answer to first part of puzzle is: {result}')
