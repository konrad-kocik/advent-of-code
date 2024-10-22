from handheld import calculate_sum_of_signal_strengths, render_image

print('\nSolving first part of puzzle')
cycles = [20, 60, 100, 140, 180, 220]
sum_of_signal_strengths = calculate_sum_of_signal_strengths('input.raw', cycles)
print(f'Answer to first part of puzzle is: {sum_of_signal_strengths}')

print('\nSolving second part of puzzle')
print(f'Answer to first part of puzzle is:')
render_image('input.raw')
