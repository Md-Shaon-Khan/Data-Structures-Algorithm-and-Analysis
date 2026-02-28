# Check if it's safe to color vertex v with color c
def is_safe(graph, color, v, c):
    for i in range(len(graph)):
        # if there is an edge from v to i and the color of i is the same as c, then it's not safe to color v with c
        if graph[v][i] == 1 and color[i] == c:
            return False
    return True

# Backtracking function to color the graph
def graph_coloring(graph, m, color, v=0): # v = current vertex index
    # Base case: all vertices are assigned a color
    if v == len(graph):
        return True

    # Try all colors from 1 to m
    for c in range(1, m+1):
        if is_safe(graph, color, v, c):
            color[v] = c  # Vertex v is assigned color c
            if graph_coloring(graph, m, color, v+1):
                return True
            color[v] = 0  # backtrack
    return False

# Test Example
graph = [
    [0, 1, 1, 1],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [1, 0, 1, 0]
]
m = 3
color = [0] * len(graph)

if graph_coloring(graph, m, color):
    print("Possible coloring:", color)
else:
    print("Not possible with", m, "colors")