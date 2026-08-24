def is_safe(node, color, graph, colors):
    for neighbor in range(len(graph)):
        if graph[node][neighbor] == 1 and colors[neighbor] == color:
            return False
    return True


def graph_coloring(graph, m, colors, node):
    if node == len(graph):
        return True

    for color in range(1, m + 1):
        if is_safe(node, color, graph, colors):
            colors[node] = color

            if graph_coloring(graph, m, colors, node + 1):
                return True

            colors[node] = 0

    return False


n = int(input("Enter number of vertices: "))

print("Enter the adjacency matrix:")
graph = []

for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

m = int(input("Enter number of colors: "))

colors = [0] * n

if graph_coloring(graph, m, colors, 0):
    print("Graph can be colored successfully.")
    print("Vertex Colors:")

    for i in range(n):
        print("Vertex", i + 1, "-> Color", colors[i])
else:
    print("Graph cannot be colored with", m, "colors.")
