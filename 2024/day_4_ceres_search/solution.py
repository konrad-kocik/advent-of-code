from word_searcher import search_word

print('\nSolving first part of puzzle')
word_count = search_word('input.raw', mode='XMAS')
print(f'Answer to first part of puzzle is: {word_count}')

print('\nSolving second part of puzzle')
word_count = search_word('input.raw', mode='X-MAS')
print(f'Answer to second part of puzzle is: {word_count}')
