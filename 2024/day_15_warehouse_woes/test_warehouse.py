from warehouse import calculate_boxes_gps_coords_sum_after_robot_movements


def test_calculate_boxes_gps_coords_sum_after_robot_movements():
    assert calculate_boxes_gps_coords_sum_after_robot_movements('test_input.raw') == 10092
