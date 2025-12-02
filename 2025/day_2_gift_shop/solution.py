from database import Database

print('Solving first part of puzzle')
database = Database()
database.load('input.raw')
invalid_product_ids = database.find_invalid_product_ids()
print(f'Answer to first part of puzzle is: {sum(invalid_product_ids)}')

print('Solving second part of puzzle')
database = Database()
database.load('input.raw')
invalid_product_ids = database.find_invalid_product_ids(advanced_search=True)
print(f'Answer to second part of puzzle is: {sum(invalid_product_ids)}')
