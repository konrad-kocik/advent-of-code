from networkx import Graph
from itertools import permutations


def find_best_arrangement(input_file_path: str, include_host: bool = False) -> int:
    relationhips_graph = _get_relationships_graph(input_file_path, include_host)
    best_arrangement_rating = _find_best_arrangement(relationhips_graph)
    return best_arrangement_rating


def _get_relationships_graph(input_file_path: str, include_host: bool) -> Graph:
    relationships = []

    with open(input_file_path) as input_file:
        for line in input_file:
            first_person, second_person = line.split()[0], line.split()[-1][:-1]
            happiness = int(line.split()[3])
            happiness = -happiness if 'lose' in line else happiness

            for relationship in relationships:
                if first_person in relationship and second_person in relationship:
                    relationship[2] += happiness
                    break
            else:
                relationships.append([first_person, second_person, happiness])

    relationships_graph = Graph()
    relationships_graph.add_weighted_edges_from(relationships)

    if include_host:
        host_relationships = [('Host', person, 0) for person in relationships_graph.nodes]
        relationships_graph.add_weighted_edges_from(host_relationships)

    return relationships_graph


def _find_best_arrangement(relationships_graph: Graph) -> int:
    best_arrangement_rating = 0
    arrangements = permutations(relationships_graph.nodes)

    for arrangement in arrangements:
        arrangement_rating = 0

        for person_id in range(len(arrangement)):
            neighbour_id = person_id + 1 if person_id + 1 < len(arrangement) else 0
            person, neighbour = arrangement[person_id], arrangement[neighbour_id]
            arrangement_rating += relationships_graph[person][neighbour]['weight']

        if arrangement_rating > best_arrangement_rating:
            best_arrangement_rating = arrangement_rating

    return best_arrangement_rating
