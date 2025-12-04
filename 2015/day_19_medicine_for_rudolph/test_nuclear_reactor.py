from pytest import mark

from nuclear_reactor import NuclearReactor


@mark.parametrize('input_file_path, expected_calibration_result', 
                  [('test_input_1.raw', 4),
                   ('test_input_2.raw', 7)])
def test_calibrate(input_file_path, expected_calibration_result):
    nuclear_reactor = NuclearReactor()
    nuclear_reactor.load_medicine_recipe(input_file_path)
    calibration_result = nuclear_reactor.calibrate()
    assert calibration_result == expected_calibration_result


@mark.parametrize('input_file_path, expected_fewest_steps', 
                  [('test_input_3.raw', 3),
                   ('test_input_4.raw', 6)])
def test_calculate_fewest_steps_to_create_medicine(input_file_path, expected_fewest_steps):
    nuclear_reactor = NuclearReactor()
    nuclear_reactor.load_medicine_recipe(input_file_path)
    fewest_steps = nuclear_reactor.calculate_fewest_steps_to_create_medicine()
    assert fewest_steps == expected_fewest_steps
