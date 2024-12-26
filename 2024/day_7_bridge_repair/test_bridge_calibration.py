from bridge_calibration import calculate_total_calibration_result


def test_calculate_total_calibration_result():
    assert calculate_total_calibration_result('test_input.raw') == 3749
