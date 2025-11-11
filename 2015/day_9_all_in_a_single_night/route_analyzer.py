from networkx import Graph
from math import inf as infinity
from itertools import permutations
from typing import Optional


def find_shortest_route(input_file_path: str) -> int:
    distances = _get_distances(input_file_path)
    shortest_route = _find_shortest_route(distances)
    return shortest_route


def _get_distances(input_file_path: str) -> Graph:
    distances = []

    with open(input_file_path, 'r') as input_file:
        for line in input_file:
            locations, distance = line.split(' = ')
            start_location, end_location = locations.split(' to ')
            distances.append((start_location, end_location, int(distance)))

    distances_graph = Graph()
    distances_graph.add_weighted_edges_from(distances)

    return distances_graph


def _find_shortest_route(distances_graph: Graph) -> int:
    shortest_distance = infinity
    potential_routes = permutations(distances_graph.nodes)

    for route in potential_routes:
        distance = _calculate_route_total_distance(route, distances_graph)

        if distance is not None and distance < shortest_distance:
            shortest_distance = distance

    return shortest_distance


def _calculate_route_total_distance(route: tuple, distances_graph: Graph) -> Optional[int]:
    distance = 0

    for i in range(len(route) - 1):
        start_location, end_location = route[i], route[i + 1]

        if distances_graph.has_edge(start_location, end_location):
            distance += distances_graph[start_location][end_location]['weight']
        else:
            return None

    return distance
