"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy
from collections import deque


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("unable to add_edge - Vertex does not exist!")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            raise IndexError("Unable to get_neighbors - not exists")

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # queue to hold nodes to visit
        # use python collection deque double ended queue
        to_visit = deque([starting_vertex])

        # set to hold the visited nodes
        visited = set()

        # while to_visit is not empty
        while len(to_visit) > 0:

            node = to_visit.pop()
            if node not in visited:
                print(node)  # sanity check while I work through
                visited.add(node)

                # add connections to visit also
                for connections in self.vertices[node]:
                    if connections not in visited:
                        to_visit.appendleft(connections)
                        visited.add(node)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # stack to hold node to visit
        to_visit = [starting_vertex]

        # set to hold visited nodes
        visited = set()

        # while the stack is not empty
        while len(to_visit) > 0:
            # pop node from stack
            v = to_visit.pop()

            # if vertex not in visited
            if v not in visited:
                # visit vertex and print for sanity check
                print(v)

                # add v to visited set
                visited.add(v)

                # add the connected vertexes to the stack
                for connected in self.vertices[v]:
                    if connected not in visited:
                        to_visit.append(connected)
                        visited.add(v)

    def dft_recursive(self, starting_vertex, visited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        # print starting vertex
        print(starting_vertex)
        visited.add(starting_vertex)

        # call dft on connections
        for conn in self.vertices[starting_vertex]:
            if conn not in visited:
                self.dft_recursive(conn, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # queue to hold nodes to visit
        # use python collection deque double ended queue
        to_visit = deque()
        to_visit.append([starting_vertex])

        # set to hold the visited nodes
        visited = set()

        # while to_visit is not empty
        while len(to_visit) > 0:

            # pop from to_visit
            path = to_visit.pop()

            # last vertex
            node = path[-1]
            # check if the vertex has been visited
            if node not in visited:
                # if node is destination
                if node == destination_vertex:
                    return path  # return path and done

                # mark it as visited
                visited.add(node)

                # add connection paths to neighbors to
                # our to_visit queue
                for connections in self.vertices[node]:

                    # make a copy and append the neighbor to the path
                    new_path = path.copy()
                    new_path.append(connections)

                    to_visit.appendleft(new_path)

        # if not path found
        return None

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # stack to hold node to visit
        to_visit = [[starting_vertex]]

        # set to hold the visited nodes
        visited = set()

        # while the stack is not empty
        while len(to_visit) > 0:
            # pop the next path
            path = to_visit.pop()

            # last vertex
            node = path[-1]

            # if node not in visited
            if node not in visited:

                # if node is destination
                if node == destination_vertex:
                    return path  # return the path

                # mark it as visited
                visited.add(node)

                # add connection paths to neighbors to
                # our to_visit queue
                for connections in self.vertices[node]:

                    # copy and append the neighbor to the path
                    new_path = path.copy()
                    new_path.append(connections)
                    to_visit.append(new_path)

        # if not path found
        return None

    def dfs_recursive(
        self, starting_vertex, destination_vertex, visited=set(), path=[]
    ):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        This should be done using recursion.
        """
        # starting vertex goes into path
        path.append(starting_vertex)
        # starting vertex goes into visited
        visited.add(starting_vertex)

        # if start is destination
        if starting_vertex == destination_vertex:
            # finished and return path
            return path

        # if the start is not the finish
        # call dfs recursively on each connection to starting_vertex
        for connections in self.vertices[starting_vertex]:
            if connections not in visited:
                p = self.dfs_recursive(
                    connections, destination_vertex, visited, path.copy()
                )
                if p is not None:
                    return p  # if a path was found, return it

        # if not found return None path
        return None


if __name__ == "__main__":
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

    """
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    """
    print(graph.vertices)

    """
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
    """
    print("*" * 25)
    print("bft 1")
    graph.bft(1)

    """
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    """
    print()
    print("*" * 25)
    print("dft 1")
    graph.dft(1)

    print()
    print("*" * 25)
    print("dft_recursive 1")
    graph.dft_recursive(1)

    """
    Valid BFS path:
        [1, 2, 4, 6]
    """
    print()
    print("*" * 25)
    print("bfs  1, 6")
    print(graph.bfs(1, 6))

    """
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    """
    print()
    print("*" * 25)
    print("dfs  1, 6 ")
    print(graph.dfs(1, 6))
    print("then dfs_recursive 1,6")
    print(graph.dfs_recursive(1, 6))
