vertices = int(input("Enter number of vertices: "))
edges_count = int(input("Enter number of edges: "))

edges = []
print("Enter edges (u v weight):")
for _ in range(edges_count):
    u, v, w = map(int, input().split())
    edges.append((u, v, w))

visited = [False] * vertices
distance = [float('inf')] * vertices

source = 0
distance[source] = 0

print("\nShortest distances from source 0:")

for _ in range(vertices):

    # Select minimum distance unvisited node
    minimum = float('inf')
    u = -1

    for i in range(vertices):
        if not visited[i] and distance[i] < minimum:
            minimum = distance[i]
            u = i

    visited[u] = True

    # Update neighbors (same edge loop style as Prim)
    for a, b, w in edges:

        if a == u and not visited[b]:
            if distance[u] + w < distance[b]:
                distance[b] = distance[u] + w

        if b == u and not visited[a]:
            if distance[u] + w < distance[a]:
                distance[a] = distance[u] + w


for i in range(vertices):
    print("0 ->", i, "=", distance[i])
    
    
# Input
# vertices = int(input("Enter number of vertices: "))
# edges_count = int(input("Enter number of edges: "))

# edges = []
# print("Enter edges (u v weight):")
# for _ in range(edges_count):
#     u, v, w = map(int, input().split())
#     edges.append((u, v, w))

# visited = [False] * vertices
# distance = [float('inf')] * vertices
# parent = [-1] * vertices

# source = 0
# distance[source] = 0

# for _ in range(vertices):

#     # Select minimum distance unvisited node
#     minimum = float('inf')
#     u = -1

#     for i in range(vertices):
#         if not visited[i] and distance[i] < minimum:
#             minimum = distance[i]
#             u = i

#     if u == -1:
#         break

#     visited[u] = True

#     # Update neighbors
#     for a, b, w in edges:

#         if a == u and not visited[b]:
#             if distance[u] + w < distance[b]:
#                 distance[b] = distance[u] + w
#                 parent[b] = u

#         if b == u and not visited[a]:
#             if distance[u] + w < distance[a]:
#                 distance[a] = distance[u] + w
#                 parent[a] = u


# print("\nShortest distances and paths from source 0:\n")

# for i in range(vertices):

#     print("0 ->", i, "Distance =", distance[i], ", Path =", end=" ")

#     # Print path
#     path = []
#     current = i
#     while current != -1:
#         path.append(current)
#         current = parent[current]

#     path.reverse()
#     print(*path, sep=" -> ")