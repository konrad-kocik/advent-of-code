from nuclear_plant import count_safe_reports

print('\nSolving first part of puzzle')
safe_reports_count = count_safe_reports('input.raw')
print(f'Answer to first part of puzzle is: {safe_reports_count}')

print('\nSolving second part of puzzle')
safe_reports_count = count_safe_reports('input.raw', problem_dampener=True)
print(f'Answer to second part of puzzle is: {safe_reports_count}')
