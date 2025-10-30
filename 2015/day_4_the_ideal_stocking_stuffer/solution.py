from crypto_miner import find_hash_producing_number

print('\nSolving first part of puzzle')
hash_producing_number = find_hash_producing_number('input.raw', leading_zeros=5)
print(f'Answer to first part of puzzle is: {hash_producing_number}')

print('\nSolving second part of puzzle')
hash_producing_number = find_hash_producing_number('input.raw', leading_zeros=6)
print(f'Answer to second part of puzzle is: {hash_producing_number}')
