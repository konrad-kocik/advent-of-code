from inventory_management_system import InventoryManagementSystem

print('Solving first part of puzzle')
inventory_management_system = InventoryManagementSystem()
inventory_management_system.load_database('input.raw')
fresh_ingredients_count = inventory_management_system.count_fresh_ingredients()
print(f'Answer to first part of puzzle is: {fresh_ingredients_count}')
