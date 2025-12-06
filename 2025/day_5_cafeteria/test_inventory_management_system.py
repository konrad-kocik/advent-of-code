from inventory_management_system import InventoryManagementSystem


def test_count_fresh_ingredients():
    inventory_management_system = InventoryManagementSystem()
    inventory_management_system.load_database('test_input.raw')
    fresh_ingredients_count = inventory_management_system.count_fresh_ingredients()
    assert fresh_ingredients_count == 3
