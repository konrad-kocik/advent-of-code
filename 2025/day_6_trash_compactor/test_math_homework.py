from pytest import fixture

from math_homework import MathHomework


@fixture
def math_homework() -> MathHomework:
    return MathHomework()


def test_math_homework(math_homework: MathHomework):
    math_homework.read('test_input.raw')
    result = math_homework.solve()
    assert result == 4277556


def test_math_homework_with_cephalopod_math(math_homework: MathHomework):
    math_homework.read('test_input.raw', cephalopod_math=True)
    result = math_homework.solve()
    assert result == 3263827
