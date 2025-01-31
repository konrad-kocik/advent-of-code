from garden import calculate_total_price_of_fence

print('\nSolving first part of puzzle')
total_price_of_fence = calculate_total_price_of_fence('input.raw')
print(f'Answer to first part of puzzle is: {total_price_of_fence}')

print('\nSolving second part of puzzle')
total_price_of_fence = calculate_total_price_of_fence('input.raw', bulk_discount=True)
print(f'Answer to second part of puzzle is: {total_price_of_fence}')
