from copy import deepcopy


def boot(file_path, cycles):
    pocket_dimension = _get_initial_pocket_dimension(file_path)
    pocket_dimension = _simulate_cycles(pocket_dimension, cycles)
    return _count_active_cubes(pocket_dimension)


def _get_initial_pocket_dimension(file_path):
    with open(file_path, 'r') as file:
        first_dimension = []

        for line in file:
            line = line.strip()
            second_dimension = []

            for char in line:
                third_dimension = [char]
                second_dimension.append(third_dimension)

            first_dimension.append(second_dimension)

    return first_dimension


def _simulate_cycles(initial_pocket_dimension, cycles_count):
    pocket_dimension = initial_pocket_dimension

    for cycle in range(1, cycles_count + 1):
        print(f'Cycle #{cycle}')
        pocket_dimension = _simulate_cycle(pocket_dimension)

    return pocket_dimension


def _simulate_cycle(pocket_dimension):
    pocket_dimension_after_cycle = deepcopy(pocket_dimension)

    for x_id, x_val in enumerate(pocket_dimension):
        for y_id, y_val in enumerate(x_val):
            for z_id, z_val in enumerate(y_val):
                coordinates = [x_id, y_id, z_id]
                state = "active" if z_val == "#" else "inactive"
                print(f'Cube {coordinates} is {state}')
                neighbours_coordinates = _get_neighbours_coordinates(coordinates)
                pocket_dimension_after_cycle = _adjust_neighbours(neighbours_coordinates, state, pocket_dimension_after_cycle)

    return pocket_dimension_after_cycle


def _get_neighbours_coordinates(coordinates):
    x, y, z = coordinates
    neighbours_coordinates = []

    for x_shift in (-1, 0, 1):
        for y_shift in (-1, 0, 1):
            for z_shift in (-1, 0, 1):
                neighbours_coordinates.append([x + x_shift, y + y_shift, z + z_shift])

    neighbours_coordinates.remove([x, y, z])
    return neighbours_coordinates


def _adjust_neighbours(neighbours_coordinates, state, pocket_dimension):

    x_size = len(pocket_dimension)
    y_size = len(pocket_dimension[0])
    z_size = len(pocket_dimension[0][0])

    x_size += 2
    y_size += 2
    z_size += 2

    from pprint import pprint
    print('Adjusted neighbours:')
    pprint(pocket_dimension)

    return pocket_dimension


def _count_active_cubes(pocket_dimension):
    count = 0

    for x in pocket_dimension:
        for y in x:
            for z in y:
                if z == '#':
                    count += 1

    return count

