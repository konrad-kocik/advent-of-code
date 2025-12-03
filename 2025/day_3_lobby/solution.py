from power_supply import PowerSupply

print('Solving first part of puzzle')
power_supply = PowerSupply()
power_supply.configure_batteries('input.raw')
total_output_joltage = power_supply.calculate_total_output_joltage()
print(f'Answer to first part of puzzle is: {total_output_joltage}')

print('Solving second part of puzzle')
power_supply = PowerSupply()
power_supply.configure_batteries('input.raw')
power_supply.override_safety()
total_output_joltage = power_supply.calculate_total_output_joltage()
print(f'Answer to second part of puzzle is: {total_output_joltage}')
