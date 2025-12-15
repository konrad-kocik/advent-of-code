from pytest import fixture, mark

from inventory_management_system import InventoryManagementSystem


@fixture
def inventory_management_system():
    ims = InventoryManagementSystem()
    ims.load_database('test_input.raw')
    return ims


def test_count_fresh_ingredients(inventory_management_system: InventoryManagementSystem):
    fresh_ingredients_count = inventory_management_system.count_fresh_ingredients()
    assert fresh_ingredients_count == 3


def test_count_all_possible_fresh_ingredients(inventory_management_system: InventoryManagementSystem):
    all_possible_fresh_ingredients = inventory_management_system.count_all_possible_fresh_ingredients()
    assert all_possible_fresh_ingredients == 14


@mark.parametrize('range_1, range_2, expected_ranges', [((102, 105), (106, 110), [(102, 105), (106, 110)]),
                                                        ((102, 105), (105, 110), [(102, 110)]),
                                                        ((102, 105), (100, 102), [(100, 105)]),
                                                        ((102, 105), (104, 115), [(102, 115)]),
                                                        ((102, 105), (100, 104), [(100, 105)]),
                                                        ((102, 110), (105, 106), [(102, 110)]),
                                                        ((105, 106), (102, 110), [(102, 110)])])
def test__merge_overlaping_fresh_ingredient_ranges(inventory_management_system: InventoryManagementSystem,
                                                   range_1: tuple[int, int],
                                                   range_2: tuple[int, int],
                                                   expected_ranges: list[tuple[int, int]]):
    inventory_management_system._fresh_ingredient_ranges = [range_1, range_2]
    inventory_management_system._merge_overlaping_fresh_ingredient_ranges()
    assert inventory_management_system._fresh_ingredient_ranges == expected_ranges
