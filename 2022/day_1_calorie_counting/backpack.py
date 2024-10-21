def find_max_calories(file_path):
    backpack = _get_backpack(file_path)
    calories = [sum(pocket) for pocket in backpack]
    return max(calories)


def get_top_three_calories_sum(file_path):
    backpack = _get_backpack(file_path)
    calories = [sum(pocket) for pocket in backpack]
    return _calculate_sum_of_top_three_values(calories)


def _get_backpack(file_path):
    backpack = []

    with open(file_path, 'r') as file:
        pocket = []

        for line in file:
            line = line.rstrip()

            if line == '':
                backpack.append(pocket)
                pocket = []
            else:
                pocket.append(int(line))

        if pocket:
            backpack.append(pocket)

    return backpack


def _calculate_sum_of_top_three_values(values):
    return sum(sorted(values)[-3:])
