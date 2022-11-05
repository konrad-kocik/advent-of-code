from jolt_calculator import calculate_jolt_differences

differences = calculate_jolt_differences('input.raw')

for difference, count in differences.items():
    print('Difference of {} was detected {} time(s)'.format(difference, count))

print('Answer to first part of puzzle is: {}'.format(differences[1] * differences[3]))
