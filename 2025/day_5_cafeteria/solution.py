from inventory_management_system import InventoryManagementSystem

print('Solving first part of puzzle')
inventory_management_system = InventoryManagementSystem()
inventory_management_system.load_database('input.raw')
fresh_ingredients_count = inventory_management_system.count_fresh_ingredients()
print(f'Answer to first part of puzzle is: {fresh_ingredients_count}')

print('Solving second part of puzzle')
inventory_management_system = InventoryManagementSystem()
inventory_management_system.load_database('input.raw')
all_possible_fresh_ingredients = inventory_management_system.count_all_possible_fresh_ingredients()
print(f'Answer to second part of puzzle is: {all_possible_fresh_ingredients}')
