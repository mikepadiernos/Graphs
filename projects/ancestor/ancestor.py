from collections import deque


def earliest_ancestor(ancestors, starting_node):
    print(ancestors)
    print(starting_node)

    queue = deque()
    queue.append([starting_node])
    graph = create_graph(ancestors)
    paths = []
    ancestor = -1
    while len(queue) > 0:
        cur_path = queue.popleft()
        cur_ancestor = cur_path[-1]
        if cur_ancestor in graph:
            for ancestor in graph[cur_ancestor]:
                new_path = list(cur_path)
                new_path.append(ancestor)
                queue.append(new_path)
        elif cur_ancestor != starting_node:
            paths.append(cur_path)

    if len(paths) > 0:
        ancestor = paths[-1][-1]
        for path in paths:
            if len(path) == len(paths[-1]):
                if ancestor > path[-1]:
                    ancestor = path[-1]

    return ancestor


def create_graph(ancestors):
    graph = {}
    for edge in ancestors:
        parent = edge[0]
        child = edge[1]
        print(parent)
        print(child)
        if child in graph:
            graph[child].add(parent)
        else:
            graph[child] = {parent}
    return graph
