from pytest import mark

from present_delivery import count_visited_houses


@mark.parametrize('input_file_path, expected_visited_houses', [('test_input_1.raw', 2),
                                                               ('test_input_2.raw', 4),
                                                               ('test_input_3.raw', 2)])
def test_count_visited_houses(input_file_path, expected_visited_houses):
    assert count_visited_houses(input_file_path) == expected_visited_houses


@mark.parametrize('input_file_path, expected_visited_houses', [('test_input_4.raw', 3),
                                                               ('test_input_2.raw', 3),
                                                               ('test_input_3.raw', 11)])
def test_count_visited_houses_with_robot_santa_deployed(input_file_path, expected_visited_houses):
    assert count_visited_houses(input_file_path, robot_santa_deployed=True) == expected_visited_houses
