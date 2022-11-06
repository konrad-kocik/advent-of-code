def calculate_manhattan_distance(file_path):
    instructions = _get_instructions(file_path)
    destination_coordinates = _calculate_destination_coordinates(instructions)
    return _calculate_manhattan_distance(destination_coordinates)


def calculate_manhattan_distance_with_waypoint(file_path):
    instructions = _get_instructions(file_path)
    destination_coordinates = _calculate_destination_coordinates_with_waypoint(instructions)
    return _calculate_manhattan_distance(destination_coordinates)


def _get_instructions(file_path):
    with open(file_path, 'r') as file:
        return [(line[0], int(line[1:])) for line in file]


def _calculate_destination_coordinates(instructions):
    moves = {
        'N': (0, 1),
        'E': (1, 0),
        'S': (0, -1),
        'W': (-1, 0)
    }

    rotations = {
        'N': {'R': {90: 'E', 180: 'S', 270: 'W'},
              'L': {90: 'W', 180: 'S', 270: 'E'}},
        'E': {'R': {90: 'S', 180: 'W', 270: 'N'},
              'L': {90: 'N', 180: 'W', 270: 'S'}},
        'S': {'R': {90: 'W', 180: 'N', 270: 'E'},
              'L': {90: 'E', 180: 'N', 270: 'W'}},
        'W': {'R': {90: 'N', 180: 'E', 270: 'S'},
              'L': {90: 'S', 180: 'E', 270: 'N'}}
    }

    ship_coordinates = [0, 0]
    ship_direction = 'E'

    for action, value in instructions:
        if action in ('N', 'E', 'S', 'W'):
            ship_coordinates[0] += moves[action][0] * value
            ship_coordinates[1] += moves[action][1] * value

        if action in ('R', 'L'):
            ship_direction = rotations[ship_direction][action][value]

        if action == 'F':
            ship_coordinates[0] += moves[ship_direction][0] * value
            ship_coordinates[1] += moves[ship_direction][1] * value

    return ship_coordinates


def _calculate_destination_coordinates_with_waypoint(instructions):
    moves = {
        'N': (0, 1),
        'E': (1, 0),
        'S': (0, -1),
        'W': (-1, 0)
    }

    ship_absolute_coordinates = [0, 0]
    waypoint_relative_coordinates = [10, 1]

    for action, value in instructions:
        if action in ('N', 'E', 'S', 'W'):
            waypoint_relative_coordinates[0] += moves[action][0] * value
            waypoint_relative_coordinates[1] += moves[action][1] * value

        if action in ('R', 'L'):
            if (action == 'R' and value == 180) or (action == 'L' and value == 180):
                waypoint_relative_coordinates = [-waypoint_relative_coordinates[0], -waypoint_relative_coordinates[1]]
            if (action == 'R' and value == 90) or (action == 'L' and value == 270):
                waypoint_relative_coordinates = [waypoint_relative_coordinates[1], -waypoint_relative_coordinates[0]]
            if (action == 'R' and value == 270) or (action == 'L' and value == 90):
                waypoint_relative_coordinates = [-waypoint_relative_coordinates[1], waypoint_relative_coordinates[0]]

        if action == 'F':
            ship_absolute_coordinates[0] += waypoint_relative_coordinates[0] * value
            ship_absolute_coordinates[1] += waypoint_relative_coordinates[1] * value

    return ship_absolute_coordinates


def _calculate_manhattan_distance(destination_coordinates):
    return abs(destination_coordinates[0]) + abs(destination_coordinates[1])
