LABEL = 0
EDGES = 1
VALUE = 2

def add_node(graph, label):
    graph.append([label, [], []])

def add_edge(graph, from_node, to_node, value):
    for node in graph:
        if node[LABEL] == from_node:
            v = node
        elif node[LABEL] == to_node:
            w = node

    v[EDGES].append(w)
    v[VALUE].append(value)
    w[EDGES].append(v)
    w[VALUE].append(value)



graph = []

add_node(graph, "a")
add_node(graph, "b")
add_node(graph, "c")
add_node(graph, "d")
print(graph)

add_edge(graph, "a", "b", 2)
add_edge(graph, "a", "c", 1)
add_edge(graph, "c", "b", 3)
add_edge(graph, "c", "b", 10)

print(graph)

