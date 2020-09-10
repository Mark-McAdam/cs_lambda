from util import Stack, Graph


def earliest_ancestor(ancestors, starting_node):
    """
    given the dataset and the ID of an individual in the dataset, 
    returns their earliest known ancestor – 
    the one at the farthest distance from the input individual. 
    If there is more than one ancestor tied for "earliest", 
    return the one with the lowest numeric ID. 
    If the input individual has no parents, the function should return -1.
    """
    # Instantiate graph, count and way to track final vertex
    graph = Graph()
    final_v = 0
    total_counter = 0

    # for people in ancestors
    # add vertex and edge
    for people in ancestors:
        graph.add_vertex(people[0])
        graph.add_vertex(people[1])

    for people in ancestors:
        graph.add_edge(people[1], people[0])

    # Instantiate Stack() to hold nodes to visit
    to_visit = Stack()
    to_visit.push(starting_node)

    # set to hold visited
    visited = set()

    # if not ancestors return -1
    # no ancestors means no neighbors so it must be own ancestor
    # -1 for being your own ancestor ... lol hillbilly - I am my own grandpa
    if len(graph.get_neighbors(starting_node)) == 0:
        return -1

    count = 0
    # so long as we have vertex to visit start popping
    while to_visit.size() > 0:
        vertex = to_visit.pop()

        if len(graph.get_neighbors(vertex)) == 0:
            if count > total_counter:
                total_counter = count
                final_v = vertex
            if count == total_counter:
                if vertex < final_v:
                    final_v = vertex

        if vertex not in visited:
            visited.add(vertex)

            if len(graph.get_neighbors(vertex)) != 0:
                for next_v in graph.get_neighbors(vertex):
                    to_visit.push(next_v)
                count += 1
            else:
                if to_visit.size() == 0:
                    return final_v

