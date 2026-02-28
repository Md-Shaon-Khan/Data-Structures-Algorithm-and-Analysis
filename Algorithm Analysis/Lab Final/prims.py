# Input
vertices = int(input("Enter number of vertices: "))
edges_count = int(input("Enter number of edges: "))

edges = []
print("Enter edges (u v weight):")
for _ in range(edges_count):
    u, v, w = map(int, input().split())
    edges.append((u, v, w))

visited = [False] * vertices
visited[0] = True   # start from vertex 0

mst_weight = 0
edge_used = 0

print("\nEdges in MST:")

while edge_used < vertices - 1:
    minimum = float('inf')
    x = y = -1

    for u, v, w in edges:
        if visited[u] and not visited[v] and w < minimum:
            minimum = w
            x, y = u, v
        if visited[v] and not visited[u] and w < minimum:
            minimum = w
            x, y = v, u

    print(x, "-", y, ":", minimum)
    mst_weight += minimum
    visited[y] = True
    edge_used += 1

print("Total weight:", mst_weight)