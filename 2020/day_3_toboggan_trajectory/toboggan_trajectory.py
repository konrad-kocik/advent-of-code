def get_trees_count(x_step, y_step):
    slope = _get_slope(x_step)
    x = 0
    y = 0
    trees_count = 0

    while y < len(slope):
        trees_count += 1 if slope[y][x] == '#' else 0
        x += x_step
        y += y_step

    return trees_count


def _get_slope(x_step):
    with open('input.raw', 'r') as file:
        lines_count = len(file.readlines())
        file.seek(0)
        return [line.rstrip() * int((x_step + 1) * lines_count / len(line.rstrip())) for line in file]


print(get_trees_count(1, 1) *
      get_trees_count(3, 1) *
      get_trees_count(5, 1) *
      get_trees_count(7, 1) *
      get_trees_count(1, 2))
