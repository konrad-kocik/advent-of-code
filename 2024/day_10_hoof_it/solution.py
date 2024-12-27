from lava_island_hiking_guide import rate_trailheads

print('\nSolving first part of puzzle')
sum_of_trailhead_scores = rate_trailheads('input.raw')
print(f'Answer to first part of puzzle is: {sum_of_trailhead_scores}')


print('\nSolving second part of puzzle')
sum_of_trailhead_ratings = rate_trailheads('input.raw', distinct_trails=True)
print(f'Answer to second part of puzzle is: {sum_of_trailhead_ratings}')
