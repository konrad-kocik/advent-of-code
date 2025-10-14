from warehouse import Warehouse

print('\nSolving first part of puzzle')
warehouse = Warehouse('input.raw')
boxes_gps_coords_sum_after_robot_movements = warehouse.calculate_boxes_gps_coords_sum_after_robot_movements()
print(f'Answer to first part of puzzle is: {boxes_gps_coords_sum_after_robot_movements}')

print('\nSolving second part of puzzle')
warehouse = Warehouse('input.raw', double_width=True)
boxes_gps_coords_sum_after_robot_movements = warehouse.calculate_boxes_gps_coords_sum_after_robot_movements()
print(f'Answer to second part of puzzle is: {boxes_gps_coords_sum_after_robot_movements}')
