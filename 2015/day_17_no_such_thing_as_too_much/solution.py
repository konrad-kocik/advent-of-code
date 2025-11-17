from refrigerator import count_possible_containers_combinations

print('Solving first part of puzzle')
possible_containers_combinations_count = count_possible_containers_combinations('input.raw', eggnog_amount=150)
print(f'Answer to first part of puzzle is: {possible_containers_combinations_count}')

print('Solving second part of puzzle')
possible_containers_combinations_count = count_possible_containers_combinations('input.raw', eggnog_amount=150, efficient_mode=True)
print(f'Answer to second part of puzzle is: {possible_containers_combinations_count}')
