from bus_scheduler import calculate_earliest_bus_hash, find_sequential_bus_departure_timestamp

print('\nSolving first part of puzzle')
earliest_bus_hash = calculate_earliest_bus_hash('input.raw')
print(f'Answer to first part of puzzle is: {earliest_bus_hash}')

print('\nSolving second part of puzzle')
bus_departure_timestamp = find_sequential_bus_departure_timestamp('input.raw', starting_timestamp=300085438130342)
print(f'Answer to second part of puzzle is: {bus_departure_timestamp}')

# old algorithm:
# 99999999999974
# 100000000000011
# 100002184945545
# 100002336517303
# 299999999999996
# 300000905528006
# 300005184188803

# new algorithm:
# 100000000000011
# 100000200658226
# 100025747090814
# 100058759821186
# -- gap
# 299999999999996
# 300005441012352
# 300034134622427
# 300049935593787
# 300055208956368
# 300063974309833
# 300085438130342
