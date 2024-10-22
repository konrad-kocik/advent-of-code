def find_shortest_path_to_destination(file_path):
    hill = _get_hill(file_path)
    path = _find_shortest_path_to_destination(hill)
    return len(path)


def _get_hill(file_path):
    with open(file_path, 'r') as file:
        grid = [line.strip() for line in file.readlines()]

    hill = {}

    for y, row in enumerate(grid):
        for x, height in enumerate(row):
            hill[(x, y, height)] = []

            for x_shift, y_shift in [(1, 0), (0, 1), (0, -1), (-1, 0)]:
                _reachable_neighbour = _check_path_to_neighbour(grid, x, y, x_shift, y_shift)

                if _reachable_neighbour:
                    hill[(x, y, height)].append(_reachable_neighbour)

    return hill


def _check_path_to_neighbour(grid, x, y, x_shift, y_shift):
    curr_height = _translate_if_start_or_end(grid[y][x])
    neighbour_x = x + x_shift
    neighbour_y = y + y_shift

    if neighbour_x < 0 or neighbour_y < 0:
        return None

    try:
        neighbour_height = _translate_if_start_or_end(grid[neighbour_y][neighbour_x])
    except IndexError:  # TODO: instead of catching error check len(grid) and len(grid[neighbour_y])
        return None

    return (neighbour_x, neighbour_y, grid[neighbour_y][neighbour_x]) if ord(neighbour_height) - ord(curr_height) <= 1 else None


def _translate_if_start_or_end(height):
    if height == 'S':
        return 'a'
    elif height == 'E':
        return 'z'
    else:
        return height


def _find_shortest_path_to_destination(graph):
    start = _find_node(graph, 'S')
    destination = _find_node(graph, 'E')
    shortest_paths = []  # TODO: this shouldn't be a list
    _search_graph(curr_node=start, path=[start], shortest_paths=shortest_paths, graph=graph, destination=destination)
    return shortest_paths[0]


def _find_node(graph, node_name):
    for node in graph.keys():
        if node[2] == node_name:
            return node


def _search_graph(curr_node, path, shortest_paths, graph, destination):
    if shortest_paths and len(path) > len(shortest_paths[0]):
        print(f'Path {path} is too long ({len(path)}), going back')
        return

    for neighbour in graph[curr_node]:
        if neighbour == destination:
            if path not in shortest_paths:
                print(f'Shortest path ({len(path)}) found: {path}')
                shortest_paths.clear()
                shortest_paths.append(path.copy())
        else:
            if neighbour not in path:
                path.append(neighbour)
                _search_graph(curr_node=neighbour,
                              path=path,
                              shortest_paths=shortest_paths,
                              graph=graph,
                              destination=destination)
                path.pop()
