set_of_node = ['A', 'B', 'C', 'D', 'E', 'F'] # PARAMETER 1
set_of_edge = {('A', 'B'): 2, ('A', 'C'): 3, ('A', 'D'): 4, ('B', 'D'): 1, ('B', 'E'): 5, ('C', 'D'): 3, ('D', 'F'): 2} # PARAMETER 2
source_node = 'C' # PARAMETER 3

def dijkstra(set_of_node: list, set_of_edge: dict, source_node = 'A'):
    path_length = {v: float('inf') for v in set_of_node}
    path_length[source_node] = 0

    adjacent_node_set = {v: {} for v in set_of_node}
    for (u, v), w_uv in set_of_edge.items():
        adjacent_node_set[u][v] = w_uv
        adjacent_node_set[v][u] = w_uv
    
    temporary_node_set = [v for v in set_of_node]
    while len(temporary_node_set) > 0:
        upper_bound = {v: path_length[v] for v in temporary_node_set}
        u = min(upper_bound, key = upper_bound.get)

        temporary_node_set.remove(u)

        for v, w_uv in adjacent_node_set[u].items():
            path_length[v] = min(path_length[v], path_length[u] + w_uv)

    for key in path_length.keys():
        print(f"THE DISTANCE OF SHORTEST PATH FROM {source_node} TO {key} IS {path_length[key]}")

    return path_length

print(dijkstra(set_of_node, set_of_edge, source_node))