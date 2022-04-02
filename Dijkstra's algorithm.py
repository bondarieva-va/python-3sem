
def generate_vertex():
    vertex = ['1', '2', '3', '4', '5', '6']
    return vertex


def set_the_vertex_connection_for_dijkstra():
    vertex_connection_for_dijkstra = {'1': {'2': 7, '3': 9, '6': 14},
                                      '2': {'1': 7, '3': 10, '4': 15},
                                      '3': {'1': 7, '4': 11, '6': 2},
                                      '4': {'2': 15, '3': 11, '5': 6},
                                      '5': {'4': 6, '6': 9},
                                      '6': {'1': 14, '3': 2, '5': 9}}
    return vertex_connection_for_dijkstra


def set_lengths_of_tracks():
    track_lengths = {'1': 100000, '2': 100000, '3': 100000,
                     '4': 100000, '5': 100000, '6': 100000}
    return track_lengths


def choice_starting_point():
    starting_point = input("Enter an initial vertex from 1 to 6: ")
    return starting_point


def set_initial_path(path, starting_point):
    path[starting_point] = 0
    return path


def dijkstras_algorithm():
    vertex_connection_for_dijkstra = set_the_vertex_connection_for_dijkstra();
    vertex = generate_vertex()
    track_lengths = set_lengths_of_tracks()
    starting_point = choice_starting_point()
    track_lengths = set_initial_path(track_lengths, starting_point)
    for i in range(6):
        for k in dict.keys(vertex_connection_for_dijkstra[vertex[i]]):
            track_lengths[k] = min(vertex_connection_for_dijkstra[vertex[i]][k] + track_lengths[vertex[i]], track_lengths[k])
    for k in dict.keys(track_lengths):
        print(starting_point, " -> ", k, '=', track_lengths[k])


def set_the_graph_for_depth_first_search():
    vertex_connection_for_dfs = {'A': {'B', 'C'},
                                 'B': {'D', 'E'},
                                 'C': {'F'},
                                 'D': {},
                                 'E': {'F'},
                                 'F': {}}
    return vertex_connection_for_dfs


def depth_first_search(vertex, vertex_connection, used=None):
    used = used or set()
    print(vertex)
    used.add(vertex)
    for neighbour in vertex_connection[vertex]:
        if neighbour not in used:
            depth_first_search(neighbour, vertex_connection, used)


def set_the_graph_for_breadth_first_search():
    vertex_connection_for_bfs = {'A': {'B', 'C'},
                                 'B': {'D', 'E'},
                                 'C': {'F'},
                                 'D': {},
                                 'E': {'F'},
                                 'F': {}}
    return vertex_connection_for_bfs


def breadth_first_search(vertex, vertex_connection, used, temp):
    used.append(vertex)
    temp.append(vertex)
    while temp:
        s = temp.pop(0)
        print(s)
        for neighbour in vertex_connection[s]:
            if neighbour not in used:
                used.append(neighbour)
                temp.append(neighbour)


def graph_bypass_option(choice):
    if choice == 1:
        dijkstras_algorithm()
    elif choice == 2:
        vertex_connection_for_dfs = set_the_graph_for_depth_first_search()
        starting_point = input('Enter an initial vertex: ')
        used = set()
        depth_first_search(starting_point, vertex_connection_for_dfs, used)
    elif choice == 3:
        vertex_connection_for_bfs = set_the_graph_for_breadth_first_search()
        starting_point = input('Enter an initial vertex: ')
        used = []
        temp = []
        breadth_first_search(starting_point, vertex_connection_for_bfs, used, temp)
    elif choice == 0:
        return -1


while True:
    choice = int(input('Enter the graph bypass option: 1 - Dijkstras algorithm, 2 - Depth-first search, 3 - Breadth-first search, 0 - End: '))
    graph_bypass_option(choice)
