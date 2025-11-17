from my_first_crime_scene_analysis_machine import match_person

print('Solving first part of puzzle')
person_id = match_person('input_evidence.raw', 'input_persons.raw')
print(f'Answer to first part of puzzle is: {person_id}')

print('Solving second part of puzzle')
person_id = match_person('input_evidence.raw', 'input_persons.raw', retroencabulator_correction=True)
print(f'Answer to second part of puzzle is: {person_id}')
