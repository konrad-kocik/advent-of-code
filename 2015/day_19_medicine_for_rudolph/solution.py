from nuclear_reactor import NuclearReactor

# print('Solving first part of puzzle')
# nuclear_reactor = NuclearReactor()
# nuclear_reactor.load_medicine_recipe('input.raw')
# calibration_result = nuclear_reactor.calibrate()
# print(f'Answer to first part of puzzle is: {calibration_result}')

print('Solving second part of puzzle')
nuclear_reactor = NuclearReactor()
nuclear_reactor.load_medicine_recipe('input.raw')
fewest_steps = nuclear_reactor.calculate_fewest_steps_to_create_medicine()
print(f'Answer to second part of puzzle is: {fewest_steps}')
