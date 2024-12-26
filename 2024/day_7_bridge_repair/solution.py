from bridge_calibration import calculate_total_calibration_result

print('\nSolving first part of puzzle')
total_calibration_result = calculate_total_calibration_result('input.raw')
print(f'Answer to first part of puzzle is: {total_calibration_result}')

print('\nSolving second part of puzzle')
total_calibration_result = calculate_total_calibration_result('input.raw', allow_concatenation=True)
print(f'Answer to second part of puzzle is: {total_calibration_result}')
