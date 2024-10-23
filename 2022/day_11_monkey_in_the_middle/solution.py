from monkey_business import calculate_level_of_monkey_business

print('\nSolving first part of puzzle')
level_of_monkey_business = calculate_level_of_monkey_business('input.raw', rounds=20)
print(f'Answer to first part of puzzle is: {level_of_monkey_business}')

print('\nSolving second part of puzzle')
level_of_monkey_business = calculate_level_of_monkey_business('input.raw', rounds=10000, worry_decrease=False)
print(f'Answer to second part of puzzle is: {level_of_monkey_business}')
