from math_homework import MathHomework


def test_math_homework():
    math_homework = MathHomework()
    math_homework.read('test_input.raw')
    result = math_homework.solve()
    assert result == 4277556
