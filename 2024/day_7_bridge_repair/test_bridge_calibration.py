from bridge_calibration import calculate_total_calibration_result


def test_calculate_total_calibration_result():
    assert calculate_total_calibration_result('test_input.raw') == 3749


def test_calculate_total_calibration_result_with_concatenation():
    assert calculate_total_calibration_result('test_input.raw', allow_concatenation=True) == 11387
