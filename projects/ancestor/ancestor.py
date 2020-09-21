from collections import deque


def earliest_ancestor(ancestors, starting_node):
    if len(ancestors) == 0:
        return

    stack = deque()
    stack.append([starting_node])
    graph, paths, ancestor = create_graph(ancestors), [], -1

    while len(stack) > 0:
        cur_path = stack.pop()
        cur_vertex = cur_path[-1]

        if cur_vertex in graph:
            for neighbor in graph[cur_vertex]:
                new_path = list(cur_path)
                new_path.append(neighbor)
                stack.append(new_path)
        elif cur_vertex != starting_node:
            paths.append(cur_path)

    if len(paths) > 0:
        ancestor = paths[-1][-1]
        for path in paths:
            if len(path) == len(paths[-1]):
                if ancestor > path[-1]:
                    ancestor = path[-1]

    return ancestor


def create_graph(ancestors):
    g = {}
    for edge in ancestors:
        origin, destination = edge[1], edge[0]
        if origin in g:
            g[origin].add(destination)
        else:
            g[origin] = {destination}
    return g
