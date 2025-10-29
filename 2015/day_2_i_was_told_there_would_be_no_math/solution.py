from wrapping_station import calculate_wrapping_paper_order,calculate_ribbon_order

print('\nSolving first part of puzzle')
wrapping_paper_order = calculate_wrapping_paper_order('input.raw')
print(f'Answer to first part of puzzle is: {wrapping_paper_order}')

print('\nSolving second part of puzzle')
ribbon_order = calculate_ribbon_order('input.raw')
print(f'Answer to second part of puzzle is: {ribbon_order}')
