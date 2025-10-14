from warehouse import Warehouse


def test_calculate_boxes_gps_coords_sum_after_robot_movements():
    warehouse = Warehouse('test_input.raw')
    assert warehouse.calculate_boxes_gps_coords_sum_after_robot_movements() == 10092


def test_calculate_boxes_gps_coords_sum_after_robot_movements_with_double_width():
    warehouse = Warehouse('test_input.raw', double_width=True)
    assert warehouse.calculate_boxes_gps_coords_sum_after_robot_movements() == 9021
