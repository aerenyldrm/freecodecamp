graph = {
    'A': [('B', 3), ('D', 1)],
    'B': [('A', 3), ('C', 4)],
    'C': [('B', 4), ('D', 7)],
    'D': [('A', 1), ('C', 7)]
}

def shortestPath(graph, start_or_source, target = ''):
    not_yet_visit = list(graph)
    distance = {key: 0 if key == start_or_source else float("inf") for key in graph}
    path_between_source_and_every_other_node = {key: [] for key in graph}
    path_between_source_and_every_other_node[start_or_source].append(start_or_source)
    while not_yet_visit:
        current = min(not_yet_visit, key = distance.get)
        for a_node, a_distance in graph[current]:
            if a_distance + distance[current] < distance[a_node]:
                distance[a_node] = a_distance + distance[current]
                if path_between_source_and_every_other_node[a_node] and path_between_source_and_every_other_node[a_node][-1] == a_node:
                    path_between_source_and_every_other_node[a_node] = path_between_source_and_every_other_node[current][:]
                else:
                    path_between_source_and_every_other_node[a_node].extend(path_between_source_and_every_other_node[current])
                path_between_source_and_every_other_node[a_node].append(a_node)
        not_yet_visit.remove(current)
    target_to_print = [target] if target else graph
    for other_node in target_to_print:
        print(f"{start_or_source} - {other_node} DISTANCE: {distance[other_node]}\nPATH: {' -> '.join(path_between_source_and_every_other_node[other_node])}\n")
    return distance, path_between_source_and_every_other_node
    
shortestPath(graph, 'A', '')