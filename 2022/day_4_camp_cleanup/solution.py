from camp import get_count_of_fully_overlapping_section_assignments, get_count_of_overlapping_section_assignments

print('\nSolving first part of puzzle')
count_of_fully_overlapping_section_assignments = get_count_of_fully_overlapping_section_assignments('input.raw')
print(f'Answer to first part of puzzle is: {count_of_fully_overlapping_section_assignments}')

print('\nSolving second part of puzzle')
count_of_overlapping_section_assignments = get_count_of_overlapping_section_assignments('input.raw')
print(f'Answer to second part of puzzle is: {count_of_overlapping_section_assignments}')
