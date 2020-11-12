from collections import deque


class Graph:
    # Represent a graph as a dictionary of vertices mapping labels to edges.
    def __init__(self):
        self.vertices = {}

    def __repr__(self):
        return str(self.vertices)

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()

    # Remove vertex from a graph and any incoming edges to it
    def remove_vertex(self, vertex_id):
        if vertex_id not in self.vertices:
            print("Attempting to remove non-existent vertex")
            return
        self.vertices.pop(vertex_id)
        for remaining_vertex in self.vertices:
            self.vertices[remaining_vertex].discard(vertex_id)

    def remove_edge(self, from_vertex_id, to_vertex_id):
        if from_vertex_id not in self.vertices or to_vertex_id not in self.vertices:
            print("Attempting to remove edges from non-existent vertex")
            return
        self.vertices[from_vertex_id].discard(to_vertex_id)

    # Adds a directed edge from "from_vertex_id" to "to_vertex_id"
    def add_edge(self, from_vertex_id, to_vertex_id):
        if from_vertex_id not in self.vertices or to_vertex_id not in self.vertices:
            print("Attempting to add edge to non-existing nodes")
            return
        self.vertices[from_vertex_id].add(to_vertex_id)

    # Returns all outgoing edges from "vertex_id"
    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        visited = set()
        queue = deque()
        queue.append(starting_vertex)
        while len(queue) > 0:
            curr_node = queue.popleft()
            if curr_node not in visited:
                neighbors = self.get_neighbors(curr_node)
                visited.add(curr_node)
                print(curr_node)
                for neighbor in neighbors:
                    queue.append(neighbor)

    def dft(self, starting_vertex):
        visited = set()
        stack = deque()
        stack.append(starting_vertex)
        while len(stack) > 0:
            curr_node = stack.pop()
            if curr_node not in visited:
                neighbors = self.get_neighbors(curr_node)
                visited.add(curr_node)
                print(curr_node)
                for neighbor in neighbors:
                    stack.append(neighbor)

    def dft_recursive(self, starting_vertex, visited=set()):
        visited.add(starting_vertex)
        print(starting_vertex)
        neighbors = self.get_neighbors(starting_vertex)
        for neighbor in neighbors:
            if neighbor not in visited:
                self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        visited = set()
        queue = deque()
        queue.append([starting_vertex])
        while len(queue) > 0:
            curr_path = queue.popleft()
            curr_node = curr_path[-1]
            neighbors = self.get_neighbors(curr_node)
            if curr_node == destination_vertex:
                return curr_path
            if curr_node not in visited:
                visited.add(curr_node)
                for neighbor in neighbors:
                    new_path = list(curr_path)
                    new_path.append(neighbor)
                    queue.append(new_path)

    # Returns a path to the goal_vertex from starting_vertex
    def dfs(self, starting_vertex, goal_vertex):
        visited = set()
        stack = deque()
        # Push the current path you're on onto the stack, instead of just a single vertex
        stack.append([starting_vertex])
        while len(stack) > 0:
            curr_path = stack.pop()
            curr_node = curr_path[-1]  # the current node you're on is the last node in the path
            if curr_node == goal_vertex:
                return curr_path
            if curr_node not in visited:
                neighbors = self.get_neighbors(curr_node)
                visited.add(curr_node)
                for neighbor in neighbors:
                    new_path = list(curr_path)  # make a copy of the current path
                    new_path.append(neighbor)
                    stack.append(new_path)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=set(), path=[]):
        visited.add(starting_vertex)
        print(starting_vertex)
        neighbors = self.get_neighbors(starting_vertex)
        path = path + [starting_vertex]
        if starting_vertex == destination_vertex:
            return path
        for neighbor in neighbors:
            if neighbor not in visited:
                new_path = self.dfs_recursive(neighbor, destination_vertex, visited, path)
                if new_path is not None:
                    return new_path


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
