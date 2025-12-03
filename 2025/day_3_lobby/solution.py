from power_supply import PowerSupply

print('Solving first part of puzzle')
power_supply = PowerSupply()
power_supply.configure_batteries('input.raw')
print(f'Answer to first part of puzzle is: {power_supply.total_output_joltage}')
